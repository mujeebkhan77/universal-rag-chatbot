from src.embeddings import get_embeddings
from src.vectorstore import load_vectorstore
from src.llm import get_llm
from src.rag import ask_question


# Load embedding model
embedding = get_embeddings()

# Load vector database
vectorstore = load_vectorstore(embedding)

# Create retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# Load Gemini
llm = get_llm()

print("🤖 YouTube Chatbot Ready!")
print("Type 'exit' to quit.\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    answer = ask_question(query, retriever, llm)

    print("\n🤖 Bot:")
    print(answer)
    print()