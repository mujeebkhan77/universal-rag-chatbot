CHROMA_PATH = "./chroma_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "gemini-2.5-flash"
TEMPERATURE = 0

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

SEPARATORS = [
    "\n\n",
    "\n",
    ".",
    "!",
    "?",
    " ",
    ""
]

SEARCH_TYPE = "mmr"
TOP_K = 5