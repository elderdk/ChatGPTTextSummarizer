from PyPDF2 import PdfReader
from pathlib import Path


def get_text_from_pdf(fpath: str) -> str:
    """Get the text from a PDF file."""

    with open(fpath, "rb") as f:
        reader = PdfReader(f)
        pages = [page.extract_text() for page in reader.pages]
        return "\n".join(pages)


if __name__ == "__main__":
    pass
