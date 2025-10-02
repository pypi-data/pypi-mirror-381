import os
import re
import uuid
import fitz
import io
import json
from tqdm import tqdm
from PIL import Image
import base64
from typing import List, Generator, Optional

import litellm
import logging

from ragformance.generators.tokenburner_gpt_2.prompts import (
    CATEGORIZE_SECTIONS_PROMPT,
    EXTRACT_TXT_PROMPT,
    FIND_CHUNKS_PROMPT,
    GENERATE_ANSWERS_PROMPT,
    GENERATE_QUESTIONS_PROMPT,
)

logger = logging.getLogger(__name__)

# Global constants for API are removed. They will be passed via args.
# MODEL_NAME = "gpt-4.1-mini" # Default can be handled in generator or main function

DEFAULT_MODEL_NAME = "gpt-4.1-mini"  # A default if not provided

# %%


def pdf_to_images(pdf_path: str) -> Generator[Image.Image, None, None]:
    doc = fitz.open(pdf_path)
    try:
        for page in doc:
            pix = page.get_pixmap()
            yield Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    finally:
        doc.close()


def image_to_bytes(image: Image.Image) -> bytes:
    with io.BytesIO() as buffer:
        image.save(buffer, format="PNG", optimize=True)
        return buffer.getvalue()


def call_backend_agent(
    system_prompt: str,
    user_prompt: str,
    api_key: str,
    base_url: str,
    model_name: str,
    temperature: float = 0.0,
    max_tokens_to_sample: int = 2000,
    stop_sequences: List[str] = None,
):
    """Call a backend LLM agent and return the answer."""
    messages = []
    if system_prompt and system_prompt.strip():
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})
    try:
        logger.info(
            f"[call_backend_agent] Calling litellm with model {model_name} at {base_url}"
        )
        response = litellm.completion(
            model="openai/" + model_name,
            messages=messages,
            api_key=api_key,
            base_url=base_url,
            temperature=temperature,
            max_tokens=max_tokens_to_sample,
            stop=stop_sequences,
        )
        if (
            response
            and hasattr(response, "choices")
            and response.choices
            and hasattr(response.choices[0], "message")
            and response.choices[0].message
            and hasattr(response.choices[0].message, "content")
            and response.choices[0].message.content
        ):
            answer = response.choices[0].message.content
            return answer
        else:
            logger.error(
                f"Error: Could not extract answer from litellm response: {response}"
            )
            return None
    except Exception as e:
        logger.error(f"Error calling litellm: {e}")
        return None


def extract_raw_text(
    image_b64: str, api_key, base_url, model: str = "MODEL_NAME"
) -> str:
    user_prompt = EXTRACT_TXT_PROMPT
    system_prompt = ""
    # Compose a multimodal message for litellm (if supported)
    # If not supported, fallback to text-only prompt
    # Here, we just pass the prompt and mention the image as base64 in the prompt
    user_prompt += f"\n[Image as base64: {image_b64[:100]}...]"  # Truncate for brevity
    return (
        call_backend_agent(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            api_key=api_key,
            base_url=base_url,
            model_name=model,
            temperature=0.0,
        )
        or ""
    )


def read_pdf_file_multimodal(
    file_path: str,
    api_key: str,
    base_url: str,
    model_name: str,
    max_pages: Optional[int] = None,
) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found")

    extracted_texts = []
    doc = fitz.open(file_path)
    total_pages = len(doc)
    pages_to_process = total_pages
    if max_pages is not None and max_pages > 0:
        pages_to_process = min(total_pages, max_pages)

    print(
        f"Converting PDF with {pages_to_process}/{total_pages} pages to images for OCR..."
    )

    for page_num, image in enumerate(pdf_to_images(file_path), start=1):
        if page_num > pages_to_process:
            break
        print(f"Processing page {page_num}/{pages_to_process}...")
        try:
            img_bytes = image_to_bytes(image)
            img_b64 = base64.b64encode(img_bytes).decode("utf-8")
            page_text = extract_raw_text(
                img_b64, api_key=api_key, base_url=base_url, model=model_name
            )
            extracted_texts.append(page_text)
        except Exception as e:
            error_msg = f"\nError processing page {page_num}: {str(e)}\n"
            extracted_texts.append(
                error_msg
            )  # Add error to list to indicate failure for this page
            print(error_msg)
    doc.close()
    print(f"OCR processing complete for {file_path}")
    return "\n\n".join(extracted_texts)


# %%


def remove_page_numbers(text: str) -> str:
    lines = text.split("\n")
    filtered_lines = [
        line for line in lines if not re.fullmatch(r"^\s*p\s*a\s*g\s*e\s+\d+\s*$", line)
    ]
    return "\n".join(filtered_lines)


# %%


def split_into_sections(raw_text: str) -> List[str]:
    section_pattern = re.compile(r"\n\s*\d+\.\s+", re.IGNORECASE)
    sections = section_pattern.split(raw_text)
    chunks = []
    for i in range(1, len(sections)):
        delimiter = section_pattern.findall(raw_text)[i - 1].strip()
        chunk = f"{delimiter}{sections[i]}".strip()
        chunks.append(chunk)
    return chunks


# %%


def convert_numbered_list_str_to_list(s: str) -> List[str]:
    pattern = re.compile(r"^\d+\.\s*")
    values = []
    for line in s.split("\n"):
        val = pattern.sub("", line).strip()
        if val:
            values.append(val)
    return values


def generate_questions(raw_text: str, api_key, base_url, model_name) -> List[str]:
    prompt = GENERATE_QUESTIONS_PROMPT.format(raw_text=raw_text)
    answer = (
        call_backend_agent(
            system_prompt="",
            user_prompt=prompt,
            api_key=api_key,
            base_url=base_url,
            model_name=model_name,
            temperature=0.0,
        )
        or ""
    )
    print(answer)
    questions = convert_numbered_list_str_to_list(answer)
    return questions


def generate_answers(context: str, query: str, api_key, base_url, model_name) -> str:
    prompt = GENERATE_ANSWERS_PROMPT.format(context=context, query=query)
    answer = (
        call_backend_agent(
            system_prompt="",
            user_prompt=prompt,
            api_key=api_key,
            base_url=base_url,
            model_name=model_name,
            temperature=0.0,
        )
        or ""
    )
    return answer.strip()


def find_chunks(context: str, query: str, api_key, base_url, model_name) -> List[str]:
    prompt = FIND_CHUNKS_PROMPT.format(context=context, query=query)
    answer = (
        call_backend_agent(
            system_prompt="",
            user_prompt=prompt,
            api_key=api_key,
            base_url=base_url,
            model_name=model_name,
            temperature=0.0,
        )
        or ""
    )
    return convert_numbered_list_str_to_list(answer.strip())


def categorize_question(query: str, context: str, api_key, base_url, model_name) -> str:
    prompt = CATEGORIZE_SECTIONS_PROMPT.format(context=context, query=query)
    answer = (
        call_backend_agent(
            system_prompt="",
            user_prompt=prompt,
            api_key=api_key,
            base_url=base_url,
            model_name=model_name,
            temperature=0.0,
        )
        or ""
    )
    return answer.strip()


def extract_category(content: str):
    category_line = next(
        line for line in content.split("\n") if line.startswith("Category: ")
    )
    match = re.search(r"Category:\s*\d+\.\s*(.*)", category_line)
    if match:
        category = match.group(1).strip()
        return category.lower()
    else:
        return "unknown"


# %%


def save_list_to_file(lf: List[str], file_path: str) -> None:
    with open(file_path, "w") as f:
        for s in lf:
            f.write(f"{s}\n")


def load_list_from_file(file_path: str) -> List[str]:
    with open(file_path) as f:
        return [line.rstrip("\n") for line in f]


# %%


# Placeholder for the refactored main logic
def main(args: dict) -> None:
    pdf_path = args["pdf_path"]
    output_dir = args["output_dir"]
    max_pages = args.get("max_pages")
    api_key = args["api_key"]
    base_url = args["base_url"]
    openai_model_name = args.get("model_name", DEFAULT_MODEL_NAME)

    print(f"Starting TokenBurner GPT-2 processing for {pdf_path}")
    print(f"Output will be saved to: {output_dir}")

    raw_extracted_text = read_pdf_file_multimodal(
        file_path=pdf_path,
        api_key=api_key,
        base_url=base_url,
        model_name=openai_model_name,
        max_pages=max_pages,
    )

    processed_text = remove_page_numbers(text=raw_extracted_text)
    sections = split_into_sections(raw_text=processed_text)

    if not sections:
        print("No sections found after text processing. Exiting.")
        open(os.path.join(output_dir, "corpus.jsonl"), "w").close()
        open(os.path.join(output_dir, "queries.jsonl"), "w").close()
        return

    # 4. Generate Corpus
    corpus_items = []
    for i, section_text in enumerate(sections):
        title = f"Section {i+1} of {os.path.basename(pdf_path)}"
        doc_id = f"doc_{os.path.basename(pdf_path)}_{i+1}"
        corpus_items.append(
            {"_id": doc_id, "title": title, "text": section_text.strip()}
        )

    corpus_file_path = os.path.join(output_dir, "corpus.jsonl")
    with open(corpus_file_path, "w", encoding="utf-8") as f_corp:
        for doc_item in corpus_items:
            f_corp.write(json.dumps(doc_item) + "\n")
    print(f"Corpus saved to {corpus_file_path}")

    # 5. Generate Queries and Answers
    query_items = []

    for doc_item in tqdm(corpus_items, desc="Generating Q&A for sections"):
        section_context = doc_item["text"]
        corpus_doc_id = doc_item["_id"]

        try:
            generated_qs = generate_questions(
                raw_text=section_context,
                api_key=api_key,
                base_url=base_url,
                model_name=openai_model_name,
            )
            for q_text in generated_qs:
                if not q_text.strip():
                    continue

                answer_text = generate_answers(
                    context=section_context,
                    query=q_text,
                    api_key=api_key,
                    base_url=base_url,
                    model_name=openai_model_name,
                )
                query_items.append(
                    {
                        "_id": str(uuid.uuid4()),
                        "question": q_text,
                        "answer": answer_text,
                        "relevant_document_ids": [
                            {"corpus_id": corpus_doc_id, "score": 1.0}
                        ],
                        "metadata": {},
                    }
                )
        except Exception as e:
            print(f"Error generating Q&A for section {corpus_doc_id}: {e}")
            query_items.append(
                {
                    "_id": str(uuid.uuid4()),
                    "question": f"Error generating question for {corpus_doc_id}",
                    "answer": str(e),
                    "relevant_document_ids": [
                        {"corpus_id": corpus_doc_id, "score": 1.0}
                    ],
                    "metadata": {"error": True},
                }
            )

    queries_file_path = os.path.join(output_dir, "queries.jsonl")
    with open(queries_file_path, "w", encoding="utf-8") as f_queries:
        for query_item in query_items:
            f_queries.write(json.dumps(query_item) + "\n")
    print(f"Queries saved to {queries_file_path}")

    print("TokenBurner GPT-2 processing finished.")
