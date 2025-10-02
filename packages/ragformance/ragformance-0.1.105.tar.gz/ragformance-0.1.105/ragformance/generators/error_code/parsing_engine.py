import json
import ast
import tiktoken
import numpy as np
import re
import litellm


class LLMClient:
    def __init__(self, llm_api_key, model, base_url):
        self.llm_api_key = llm_api_key
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str) -> str:
        return (
            litellm.completion(
                model="openai/" + self.model,
                base_url=self.base_url,
                api_key=self.llm_api_key,
                messages=[{"content": prompt, "role": "user"}],
            )
            .choices[0]
            .message.content.strip()
        )


def estimate_tokens(text: str) -> int:
    """Estimate the number of tokens in a text using tiktoken."""
    tokenizer = tiktoken.get_encoding("cl100k_base")
    return len(tokenizer.encode(text))


def split_document(
    document: str, max_tokens: int = 160000, overlap_chars: int = 4000
) -> list:
    """Split a document into chunks based on max token count and overlap."""
    avg_token_length = 4
    max_chars = max_tokens * avg_token_length
    chunks = []
    start, end = 0, 0
    while end < len(document):
        end = min(start + max_chars, len(document))
        chunk = document[start:end]
        chunks.append(chunk)
        start = end - overlap_chars
    return chunks


def find_pages(
    keyword: str,
    document: str,
    max_token_context: int = 64000,
    API_KEY: str = None,
    API_URL: str = "https://openrouter.ai/api/v1/chat/completions",
    API_MODEL: str = "qwen/qwen3-32b:free",
) -> list:
    """Find pages in a document that mention a keyword using an LLM API."""
    if not API_KEY:
        raise ValueError("Please set the API_KEY environment variable.")
    estimated_tokens = estimate_tokens(document)
    print("estimated_tokens", estimated_tokens)
    if estimated_tokens > max_token_context:
        print("Document too large, splitting into chunks...")
        chunks = split_document(document, max_tokens=max_token_context - 4000)
    else:
        chunks = [document]
    all_pages = []
    llm = LLMClient(API_KEY, API_MODEL, API_URL)
    for i, chunk in enumerate(chunks):
        prompt = (
            "The following is the content of a Markdown file:\n\n"
            f"{chunk}\n\n"
            f"Please analyze this content and identify the pages that talk about {keyword}. "
            "Return only the page numbers as a Python list (e.g., [35,36,37]). if you don't find any pages (which often happens), just return []."
        )
        try:
            message = llm.generate(prompt)
            match = re.search(r"\[.*?\]", message).group()
            page_numbers = ast.literal_eval(match)
            if isinstance(page_numbers, list) and all(
                isinstance(num, int) for num in page_numbers
            ):
                all_pages.extend(page_numbers)
            else:
                print(f"Response from chunk {i} is not a valid list of integers.")
        except Exception as e:
            print(f"Error parsing response from chunk {i}: {e}")

    # rework pages : should probably just filter on the chunks
    return list(np.unique(all_pages)) if all_pages else None


def merge_pages(
    page_numbers: list, path: str, prefix_id: str, title: str, manual_text: str = ""
) -> tuple:
    """Merge selected pages into a single text and build a corpus list."""
    # TODO rework page logic to handle different folder structure
    selected_pages = []
    corpus = []

    # split manual_text into pages if provided
    if manual_text:
        manual_pages = manual_text.split("\n## ")
        for page, text in enumerate(manual_pages):
            selected_pages += f"\n\n --- PAGE n°{page} --- \n\n"
            selected_pages += text
            corpus.append(
                {"_id": f"DOC_{prefix_id}_p{page}", "title": title, "text": text}
            )
    else:
        for page in page_numbers:
            with open(path + f"/page_{page}.md", encoding="utf-8") as file:
                selected_pages += f"\n\n --- PAGE n°{page} --- \n\n"
                text = file.read()
                selected_pages += text
                corpus.append(
                    {"_id": f"DOC_{prefix_id}_p{page}", "title": title, "text": text}
                )
    pages_as_string = "".join(selected_pages)
    return pages_as_string, corpus


def extract_keywords(
    keyword: str,
    document: str,
    API_KEY: str = None,
    API_URL: str = "https://openrouter.ai/api/v1/chat/completions",
    API_MODEL: str = "qwen/qwen3-32b:free",
    max_token_context: int = 64000,
) -> dict:
    """Extract keywords and their context from a document using an LLM API, with chunking support for large documents."""
    if not API_KEY:
        raise ValueError("Please set the API_KEY environment variable.")
    llm = LLMClient(API_KEY, API_MODEL, API_URL)
    estimated_tokens = estimate_tokens(document)
    results = {}
    if estimated_tokens > max_token_context:
        print("Document too large, splitting into chunks for keyword extraction...")
        chunks = split_document(document, max_tokens=max_token_context - 4000)
    else:
        chunks = [document]
    for i, chunk in enumerate(chunks):
        prompt = (
            "You are a text analysis assistant.\n"
            f"Given the following text, identify all {keyword} present. For each error code, extract the exact sentence or paragraph in which it appears, ensuring the text remains unaltered. Don't forget to add the page where the sentence has been extracted. Return the results in a JSON format where each key is an error code, and its value is the corresponding text segment, and it's associate page number."
            f"Even if you're not sure but it seems to be a {keyword}, don't hesitate to put it in doubt."
            "Example output format:\n"
            """{
            "ERROR_CODE_1": ["Exact text containing ERROR_CODE_1", X1 (corresponding to the page number of the extract text)],
            "ERROR_CODE_2": ["Exact text containing ERROR_CODE_2.", X2 (corresponding to the page number of the extract text)],
            ...
            }"""
            f"Text to analyse: {chunk}"
        )
        try:
            message = llm.generate(prompt)
            print(f"Raw response from the model for chunk {i}:")
            chunk_result = json.loads(message)
            if isinstance(chunk_result, dict):
                for k, v in chunk_result.items():
                    # Si la clé existe déjà, on ajoute les nouveaux extraits
                    if (
                        k in results
                        and isinstance(results[k], list)
                        and isinstance(v, list)
                    ):
                        results[k].extend(v)
                    else:
                        results[k] = v
        except Exception as e:
            print(f"Error during LLM call for chunk {i}: {e}")
    return results if results else None
