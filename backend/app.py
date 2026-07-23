import os
import streamlit as st
from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from src.utils import extract_video_id
from src.rag import ask_question

load_dotenv()

st.set_page_config(page_title="YouTube AI Assistant", layout="wide")
st.markdown("""
    <style>
        .stChatMessage {
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)
# ---------------- CACHE MODELS ----------------
@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

@st.cache_resource
def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )

embedding = get_embeddings()
llm = get_llm()

# ---------------- SESSION INIT ----------------
if "video_ready" not in st.session_state:
    st.session_state.video_ready = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🎥 YouTube AI")

    url = st.text_input("Paste YouTube URL")

    if st.button("📥 Load Video"):

        video_id = extract_video_id(url)

        if not video_id:
            st.error("Invalid URL")
        else:
            with st.spinner("Processing video..."):

                # 1. Transcript
                transcript = YouTubeTranscriptApi().fetch(video_id)
                text = " ".join([t.text for t in transcript])

                # 2. Split
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=100
                )
                chunks = splitter.split_text(text)

                # 3. Embeddings
                vectorstore = Chroma.from_texts(
                    texts=chunks,
                    embedding=embedding,
                    persist_directory=f"./chroma_db/{video_id}"
                )

                # 4. Retriever
                retriever = vectorstore.as_retriever(
                    search_type="similarity",
                    search_kwargs={"k": 5}
                )

                # store in session
                st.session_state.retriever = retriever
                st.session_state.video_ready = True
                st.session_state.video_id = video_id

            st.success("Video loaded successfully!")

    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []

# ---------------- MAIN UI ----------------
st.title("💬 Chat with YouTube Video")

if not st.session_state.video_ready:
    st.warning("Load a YouTube video first.")
    st.stop()

# ---------------- CHAT HISTORY ----------------
for role, msg in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(f"🧑 {msg}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"🤖 {msg}")

# ---------------- INPUT ----------------
query = st.chat_input("Ask anything about the video...")

if query:

    st.session_state.chat_history.append(("user", query))

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):

            answer = ask_question(
                query,
                st.session_state.retriever,
                llm
            )

        st.markdown(answer)

    st.session_state.chat_history.append(("assistant", answer))