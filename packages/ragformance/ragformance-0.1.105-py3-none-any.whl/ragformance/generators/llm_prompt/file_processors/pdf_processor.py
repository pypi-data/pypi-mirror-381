from pathlib import Path
from typing import List
from ragformance.generators.llm_prompt.file_processors.file_processor_interface import (
    FileProcessor,
)
from ragformance.models.corpus import DocModel
from ragformance.generators.utils.pdf_utils import extract_pdf_with_fitz


class PdfProcessor(FileProcessor):
    def can_process(self, file_path: Path) -> bool:
        return file_path.suffix.lower() == ".pdf"

    def process(self, file_path: Path) -> List[DocModel]:
        return extract_pdf_with_fitz(file_path)
