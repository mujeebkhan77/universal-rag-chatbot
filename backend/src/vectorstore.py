from langchain_chroma import Chroma
from src.config import CHROMA_PATH

def create_vectorstore(chunks, embedding):
    """
    Create Chroma database from document chunks.
    """

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=CHROMA_PATH
    )

    return vectorstore

def load_vectorstore(embedding):
    """
    Load existing Chroma database.
    """

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding
    )

    return vectorstore


def get_documents(embedding):

    vectorstore = load_vectorstore(embedding)

    data = vectorstore.get()

    metadata_list = data["metadatas"]

    documents = {}

    for metadata in metadata_list:

        document_id = metadata["document_id"]

        if document_id not in documents:

            documents[document_id] = {
                "name": metadata["file"],
                "type": metadata["source"],
                "document_id": document_id
            }

    return list(documents.values())

def delete_document(embedding, document_id):

    vectorstore = load_vectorstore(embedding)

    data = vectorstore.get(
        where={
            "document_id": document_id
        }
    )

    print("DELETE ID:", document_id)
    print("FOUND IDS:", data["ids"])

    ids = data["ids"]

    if ids:
        vectorstore.delete(ids=ids)

    return True