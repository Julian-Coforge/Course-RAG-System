from pathlib import Path
from pypdf import PdfReader

def extract_pdf(path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        path (str): The path to the PDF file.
    """

    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append({
                "source": Path(path).name,
                "page_number": i + 1,
                "text": text
            })
    return pages

if __name__ == "__main__":
    pages = extract_pdf("/Users/Julian.Marchington/Desktop/Week 1 Exam/Coding Best Practices.pdf")
    print(f"Extracted {len(pages)} pages from the PDF.")
    print(pages[0]["text"])  # Print the text of the first page