from typing import List
from ragformance.models.corpus import DocModel
from pathlib import Path
import os


# Fonction centrale de détection et extraction/conversion PDF
def _extract_pdf_content(file_path, as_docmodel=False):
    """
    Fonction centrale qui choisit dynamiquement la meilleure méthode disponible pour extraire le contenu d'un PDF.
    - as_markdown : retourne du markdown si possible
    - as_docmodel : retourne une liste de DocModel si possible
    """
    # 2. Tenter unstructured pour texte brut
    try:
        from unstructured.partition.auto import partition

        elements = partition(file_path)
        text = "\n".join(e.text for e in elements if getattr(e, "text", ""))
        if as_docmodel:
            name = Path(file_path).stem
            return [
                DocModel(
                    _id=f"{name}-all",
                    title=name,
                    text=text,
                    metadata={"document_id": name},
                )
            ]
        return [text]  # fallback markdown = texte brut
    except ImportError:
        pass
    # 3. Tenter langchain PyPDFLoader
    try:
        from langchain.document_loaders import PyPDFLoader

        loader = PyPDFLoader(file_path)
        documents = loader.load()
        if as_docmodel:
            name = Path(file_path).stem
            return [
                DocModel(
                    _id=f"{name}-page={i+1}",
                    title=name,
                    text=doc.page_content,
                    metadata={"document_id": name, "page_number": i + 1},
                )
                for i, doc in enumerate(documents)
            ]
        return [doc.page_content for doc in documents]
    except Exception:
        pass
    # 4. Tenter fitz (PyMuPDF)
    try:
        import fitz  # PyMuPDF

        doc = fitz.open(str(file_path))
        name = Path(file_path).stem
        results = []
        for page_num in range(len(doc)):
            text = doc.load_page(page_num).get_text().strip()
            if as_docmodel:
                results.append(
                    DocModel(
                        _id=f"{name}-page={page_num + 1}",
                        title=name,
                        text=text,
                        metadata={"document_id": name, "page_number": page_num + 1},
                    )
                )
            else:
                results.append(text)
        doc.close()
        return results
    except Exception:
        pass
    # Si rien n'est dispo
    raise ImportError(
        "Aucune bibliothèque compatible pour extraire le contenu du PDF n'est installée. Veuillez installer forcolate, unstructured, langchain ou pymupdf."
    )


def convert_folders_to_markdown(query="", folder_in="", folder_out=""):
    try:
        from forcolate import convert_folders_to_markdown

        return convert_folders_to_markdown(query="", folder_in="", folder_out="")

    except ImportError:
        pass

    # we call the central function to extract text for all files in the folder with os.walk
    for root, _, files in os.walk(folder_in):
        for file in files:
            if file.endswith(".pdf"):
                file_path = Path(root) / file
                try:
                    contents = _extract_pdf_content(file_path)
                    # Write contents to markdown file
                    md_file_path = Path(folder_out) / (file.replace(".pdf", ".md"))
                    with open(md_file_path, "w", encoding="utf-8") as md_file:
                        for content in contents:
                            md_file.write(content + "\n\n")
                except ImportError as e:
                    print(f"Error processing {file}: {e}")


def extract_contents(file_path: str) -> str:
    return _extract_pdf_content(file_path)


def load_pdf_documents(pdf_path: str) -> List[str]:
    return _extract_pdf_content(pdf_path)


def extract_pdf_with_fitz(file_path: Path) -> List[DocModel]:
    return _extract_pdf_content(str(file_path), as_docmodel=True)
