from pathlib import Path
from pdfReader import extract_pdf

def chunk_pages(pages, chunk_size=500, overlap=100):
    """
    Chunks the extracted pages into smaller segments.

    Args:
        pages (list): A list of dictionaries containing page information.
        chunk_size (int): The maximum number of characters in each chunk.
        overlap (int): The number of overlapping characters between chunks.
    """

    step = chunk_size - overlap
    chunks = []
    for page in pages:
        text = page["text"]
        for start in range(0, len(text), step):
            piece = text[start:start + chunk_size].strip()
            if len(piece) < 50:  # Skip very small chunks
                continue
            chunks.append({
                "id": len(chunks),
                "source": page["source"],
                "page_number": page["page_number"],
                "chunk_text": piece
            })
    return chunks

if __name__ == "__main__":
    all_pages = []
    for pdf in sorted(Path("docs").glob("*.pdf")):
        all_pages.extend(extract_pdf(pdf))

    chunks = chunk_pages(all_pages)
    print(f"{len(all_pages)} pages -> {len(chunks)} chunks")
    for c in chunks[:3]:
        print(f"\n[{c['id']}] {c['source']} p.{c['page']}")
        print(c["text"])