from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHUNK_SIZE, CHUNK_OVERLAP, SEPARATORS

def split_documents(documents):
    """
    Split documents into meaningful chunks.
    Keeps metadata.
    """

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=SEPARATORS
)

    chunks = splitter.split_documents(
        documents
    )

    return chunks