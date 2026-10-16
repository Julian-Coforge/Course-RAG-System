from pathlib import Path
from pypdf import PdfReader

def extract_pdf(path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        path (str): The path to the PDF file.
    """
    