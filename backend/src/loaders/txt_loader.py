from langchain_core.documents import Document
from pathlib import Path
import uuid


def load_txt(file_path: str):
    """
    Extract text from TXT file.

    Returns:
        List of LangChain Documents
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    document_id = str(uuid.uuid4())

    document = Document(
        page_content=text,
        metadata={
            "document_id": document_id,
            "source": "txt",
            "file": Path(file_path).name,
        }
    )

    return [document]