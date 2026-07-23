from src.embeddings import get_embeddings
from src.vectorstore import load_vectorstore
from src.llm import get_llm
from src.rag import ask_question
from src.config import SEARCH_TYPE, TOP_K

embedding = get_embeddings()

vectorstore = load_vectorstore(embedding)

retriever = vectorstore.as_retriever(
    search_type=SEARCH_TYPE,
    search_kwargs={
        "k": TOP_K
    }
)

llm = get_llm()

print("\n🤖 RAG Chatbot Ready")
print("Type 'exit' to stop\n")

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    result = ask_question(query, retriever, llm)

    # Print answer
    print("\n🤖 AI:")
    print(result["answer"])

    # Print sources
    print("\n📚 Sources:")

    if not result["sources"]:
        print("No sources found.")
    else:
        for source in result["sources"]:

            if source["source"] == "youtube":
                print(
                    f"▶️ YouTube Video ID: {source['video_id']}"
                )

            elif source["source"] == "pdf":
                print(
                    f"📄 {source['file']} (Page {source['page']})"
                )

            else:
                print(source)

    print("-" * 60)