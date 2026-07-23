from src.loaders.youtube_loader import load_youtube_transcript
from src.loaders.pdf_loader import load_pdf
from src.loaders.docx_loader import load_docx
from src.loaders.txt_loader import load_txt

from src.splitter import split_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore


def ingest_youtube(video_id: str):
    """
    Ingest a YouTube video into ChromaDB.
    """

    documents = load_youtube_transcript(video_id)

    chunks = split_documents(documents)

    embedding = get_embeddings()

    create_vectorstore(chunks, embedding)


def ingest_pdf(file_path: str):
    """
    Ingest a PDF into ChromaDB.
    """

    documents = load_pdf(file_path)

    chunks = split_documents(documents)

    embedding = get_embeddings()

    create_vectorstore(chunks, embedding)
    
def ingest_docx(file_path: str):

    documents = load_docx(file_path)

    chunks = split_documents(documents)

    embedding = get_embeddings()
    
    create_vectorstore(chunks, embedding)


def ingest_txt(file_path: str):

    documents = load_txt(file_path)

    chunks = split_documents(documents)

    embedding = get_embeddings()

    create_vectorstore(chunks, embedding)