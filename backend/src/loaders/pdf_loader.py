from pypdf import PdfReader
from langchain_core.documents import Document

from pathlib import Path
import uuid

def load_pdf(file_path: str):
    """
    Extract text from PDF.

    Returns:
        List of LangChain Documents
    """

    reader = PdfReader(file_path)

    documents = []

    document_id =str(uuid.uuid4())
    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text:

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "document_id" : document_id,
                        "source": "pdf",
                        "page": page_number,
                        "file": Path(file_path).name,
                    }
                )
            )

    return documents