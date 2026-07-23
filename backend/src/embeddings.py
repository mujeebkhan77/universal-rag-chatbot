from langchain_huggingface import HuggingFaceEmbeddings
from src.config import EMBEDDING_MODEL

def get_embeddings():
    """
    Load embedding model.
    """

    embedding = HuggingFaceEmbeddings(
        model_name= EMBEDDING_MODEL
    )

    return embedding