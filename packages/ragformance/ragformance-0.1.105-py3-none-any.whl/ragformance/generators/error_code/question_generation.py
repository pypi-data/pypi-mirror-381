import json
import string
import numpy as np

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


def question_variation(
    question,
    nombre_variantes=5,
    API_KEY="api_key",
    API_URL="api_url",
    API_MODEL="api_model",
):
    """
    Generates linguistic variations of a given question using an LLM client.
    The output is structured in JSON for easy automatic retrieval.
    """
    llm_client = LLMClient(API_KEY, API_MODEL, API_URL)

    prompt = (
        "You are an expert assistant in question rephrasing.\n"
        "Your task is to generate varied linguistic rephrasings for a batch of given questions in the following format:\n"
        '{"_id": ID1, "query_text": QUESTION1}\n'
        '{"_id": ID2, "query_text": QUESTION2}\n'
        "...\n"
        "Strictly preserve the meaning of the original question, while changing the style, phrasing, or vocabulary. You must formulate questions as if a member of the general public were asking them.\n"
        f'Here is the list of questions: "{question}"\n\n'
        f"Generate exactly {nombre_variantes} variations.\n"
        "Return only the answer in the following JSON format:\n"
        '{ID1: ["VARIATION1", "VARIATION2", "..."], ID2: ["VARIATION1", "VARIATION2", "..."]}'
    )

    try:
        message = llm_client.generate(prompt)
        # Try to directly parse the JSON response
        message = json.loads(message)
        return message
    except Exception as e:
        print(f"Error during call or parsing: {e}")
        return {}


# Write to JSONL
def generate_easy_question(tabular_data, category="None", tags=["None"], prefix_id=""):
    output, query_augmentation = [], []

    for idx, (error_code, (text, page_num)) in enumerate(tabular_data.items(), start=1):
        json_obj = {
            "_id": f"{prefix_id}_EASY_{idx}",
            "query_text": f"What does error code {error_code} mean?",
            "relevant_document_ids": [
                {"corpus_id": f"DOC_{prefix_id}_p{page_num}", "score": 1}
            ],
            "ref_answer": text,
            "metadata": {"category": category, "difficulty": "Easy", "tags": tags},
        }
        query_augmentation.append(
            {
                "_id": f"{prefix_id}_EASY_{idx}",
                "query_text": f"What does error code {error_code} mean?",
            }
        )
        output.append(json_obj)

    return output, query_augmentation


def generate_med_question(
    tabular_data,
    document,
    category="None",
    tags=["None"],
    prefix_id="",
    API_KEY="api_key",
    API_URL="api_url",
    API_MODEL="api_model",
):
    output, query_augmentation = [], []

    llm_client = LLMClient(API_KEY, API_MODEL, API_URL)

    for idx, (error_code, (text, page_num)) in enumerate(tabular_data.items(), start=1):
        prompt = (
            "You are a text analysis assistant.\n"
            f"Given the following troubleshoot, identify all the different steps for solving the problem. For each step, extract the exact sentence or paragraph in which it appears, ensuring the text remains unaltered. Don't forget to add the page where the sentence has been extracted. Return the results in a JSON format including all the steps and their associated page numbers.\n"
            "Example output format:\n"
            """{\n
                \"result\": \"1.EXTRACT_TEXT1 \n 2.EXTRACT_TEXT2 \n 3. ...\",\n
                \"page\": [PAGE1, PAGE2, ...],\n
                ...\n
                }\n"""
            "where PAGE1 corresponds to the page where EXTRACT_TEXT1 has been extracted, PAGE2 for EXTRACT_TEXT2, ...\n"
            "The troubleshoot may not be indicated in the document. In this case, return an empty json (i.e., {})\n"
            f"Troubleshoot to address: {text}\n\n"
            f"Text to analyse: {document}"
        )
        try:
            message = llm_client.generate(prompt)
            if message.strip() == "{}":
                continue
            message = json.loads(message)
            all_pages = message["page"]
            all_pages.append(page_num)
            json_obj = {
                "_id": f"{prefix_id}_MED_{idx}",
                "query_text": f"What are the steps to solve the problem related to error code {error_code}?",
                "relevant_document_ids": [
                    {"corpus_id": f"DOC_{prefix_id}_p{i}", "score": 1}
                    for i in np.unique(all_pages)
                ],
                "ref_answer": message["result"],
                "metadata": {
                    "category": category,
                    "difficulty": "Medium",
                    "tags": tags,
                },
            }
            query_augmentation.append(
                {
                    "_id": f"{prefix_id}_MED_{idx}",
                    "query_text": f"What are the steps to solve the problem related to error code {error_code}?",
                }
            )
            output.append(json_obj)
        except Exception as e:
            print(f"Error during call or parsing: {e}")
            continue
    return output, query_augmentation


# Supposons que `output` et `augmented_question` soient des chaînes de texte contenant du JSONL
# Exemple :
# output = '...'
# augmented_question = '...'
def add_augmented_question(main_data, variations_data):
    # Étape 2 : générer la liste finale d'objets
    final_entries = []

    for entry in main_data:
        base_id = entry["_id"]
        final_entries.append(entry)  # Ajouter la version principale

        # Ajouter les variations s'il y en a
        if base_id in variations_data:
            variations = variations_data[base_id]
            for idx, variation in enumerate(variations):
                letter = string.ascii_lowercase[idx]  # a, b, c, ...
                new_entry = entry.copy()
                new_entry["_id"] = f"{base_id}{letter}"
                new_entry["query_text"] = variation
                final_entries.append(new_entry)

    return final_entries
