import re
import json
from typing import Any
import logging

logger = logging.getLogger(__name__)

# TODO : uniformize answer parsing across generators


def extract_content_from_xml_tags(full_content: str, xml_tag: str) -> str:
    """Extract the content between the XML tags."""
    pattern_with_closing_tag = f"<{xml_tag}>(.*?)</{xml_tag}>"
    pattern_without_closing_tag = f"<{xml_tag}>(.*)"
    try:
        matches_with_closing = re.findall(
            pattern_with_closing_tag, full_content, re.DOTALL
        )
        if matches_with_closing:
            return matches_with_closing[0].strip()
        matches_without_closing = re.findall(
            pattern_without_closing_tag, full_content, re.DOTALL
        )
        if matches_without_closing:
            return matches_without_closing[0].strip()
        return ""
    except Exception as extraction_error:
        logger.error(f"Error extracting content from XML tags: {extraction_error}")
        return ""


def parse_qa_pairs_from_response(raw_response: str) -> list[dict[str, Any]]:
    """
    Attempt to parse question-answer pairs from a raw LLM response.
    The function searches in this priority order:
        1. <output_json>...</output_json> tags.
        2. ```json fenced code blocks.
        3. Best-effort bracket-based extraction.
    If any candidate JSON is found, it attempts to parse it. If parsing
    succeeds and yields a list, it returns that list. Otherwise, it
    returns an empty list.
    Even if this returns an empty list, callers are expected to store
    the raw response (e.g., so the pipeline does not lose data).
    Args:
        raw_response (str): The complete raw response string from the model.
    Returns:
        A list of dict objects, each presumably containing
        question-answer information. If no valid parse is found,
        an empty list is returned.
    """
    if not raw_response or not isinstance(raw_response, str):
        return []
    extracted_json_str = _extract_tag_content(raw_response, "output_json")
    if extracted_json_str.strip():
        possible_parsed = _attempt_json_parse(
            _maybe_strip_triple_backticks(extracted_json_str)
        )
        if isinstance(possible_parsed, list):
            return possible_parsed
    fence_pattern = r"```json\s*([\s\S]*?)\s*```"
    fence_match = re.search(fence_pattern, raw_response)
    if fence_match:
        possible_parsed = _attempt_json_parse(fence_match.group(1).strip())
        if isinstance(possible_parsed, list):
            return possible_parsed
    bracket_candidates = _best_effort_json_extract(raw_response)
    for candidate in bracket_candidates:
        possible_parsed = _attempt_json_parse(candidate)
        if isinstance(possible_parsed, list):
            return possible_parsed
    return []


def _extract_tag_content(text: str, tag: str) -> str:
    """Extract text enclosed in <tag>...</tag> from the given string."""
    try:
        pattern = rf"<{tag}\s*>([\s\S]*?)</{tag}>"
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    except Exception as e:
        logger.error(f"Error extracting tag content for '{tag}': {e}")
    return ""


def _maybe_strip_triple_backticks(text_in: str) -> str:
    """Removes triple backticks (``` or ```json) from the beginning and end of a string, if present."""
    if not text_in or not isinstance(text_in, str):
        return ""
    try:
        pattern = r"^\s*```(?:json)?\s*([\s\S]*?)\s*```$"
        match = re.match(pattern, text_in)
        if match:
            return match.group(1)
    except Exception as e:
        logger.error(f"Error stripping backticks: {e}")
    return text_in


def _best_effort_json_extract(full_text: str) -> list[str]:
    """Collect bracket-delimited substrings that might be valid JSON."""
    if not full_text or not isinstance(full_text, str):
        return []
    candidates = []
    try:
        pattern = r"([\[{].*?[\]}])"
        matches = re.findall(pattern, full_text, flags=re.DOTALL)
        for match_text in matches:
            if (match_text.startswith("[") and match_text.endswith("]")) or (
                match_text.startswith("{") and match_text.endswith("}")
            ):
                candidates.append(match_text.strip())
    except Exception as e:
        logger.error(f"Error in best-effort JSON extraction: {e}")
    return candidates


def _attempt_json_parse(json_str: str) -> Any:
    """Attempt to parse a JSON string. Return parsed object if success, or None if parsing fails."""
    try:
        return json.loads(json_str)
    except Exception:
        return None
