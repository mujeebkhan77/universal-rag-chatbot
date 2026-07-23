from fastapi import FastAPI
from pydantic import BaseModel

from src.embeddings import get_embeddings
from src.vectorstore import load_vectorstore,get_documents,delete_document
from src.llm import get_llm
from src.rag import ask_question
from src.config import SEARCH_TYPE, TOP_K

from src.ingestion import ingest_youtube,ingest_pdf
from src.ingestion import ingest_docx, ingest_txt
from src.utils import extract_video_id

from fastapi import UploadFile, File
import shutil
from pathlib import Path

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Universal RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = Path("uploads/pdf")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

embedding = None
vectorstore = None
retriever = None
llm = None


def load_rag():
    global embedding, vectorstore, retriever, llm

    if retriever is None:
        # embedding = get_embeddings()

        # vectorstore = load_vectorstore(embedding)

        # retriever = vectorstore.as_retriever(
        #     search_type=SEARCH_TYPE,
        #     search_kwargs={"k": TOP_K}
        # )

        llm = get_llm()

    return retriever, llm, embedding

class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Universal RAG API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    return {"message": "Server is running"}

class YoutubeRequest(BaseModel):
    url: str
    
    
@app.post("/ingest/youtube")
def ingest(request: YoutubeRequest):

    video_id = extract_video_id(request.url)

    if video_id is None:
        return {
            "success": False,
            "message": "Invalid YouTube URL."
        }

    ingest_youtube(video_id)

    return {
        "success": True,
        "message": "Video ingested successfully."
    }    
    
@app.post("/ingest/file")
def upload_file(file: UploadFile = File(...)):

    save_path = UPLOAD_FOLDER / file.filename

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extension = file.filename.split(".")[-1].lower()
    print("FILE TYPE:", extension)
    if extension == "pdf":
        ingest_pdf(str(save_path))

    elif extension == "docx":
        ingest_docx(str(save_path))

    elif extension == "txt":
        ingest_txt(str(save_path))

    else:
        return {
            "success": False,
            "message": "Unsupported file type."
        }

    return {
        "success": True,
        "message": f"{file.filename} uploaded successfully."
    } 
    
     
@app.get("/documents")
def documents():
       
       data =  get_documents(embedding)
       
       return data
   
@app.delete("/documents/{document_id}")
def delete_doc(document_id: str):

    delete_document(embedding, document_id)

    return {
        "success": True,
        "message": "Document deleted successfully"
    }  
    
    
print("STEP 1")

embedding = get_embeddings()
print("STEP 2")

vectorstore = load_vectorstore(embedding)
print("STEP 3")

retriever = vectorstore.as_retriever(
    search_type=SEARCH_TYPE,
    search_kwargs={"k": TOP_K}
)
print("STEP 4")

llm = get_llm()
print("STEP 5")    