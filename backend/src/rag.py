def ask_question(query, retriever, llm):
    """
    Ask a question using the RAG pipeline.

    Returns:
        {
            "answer": "...",
            "sources": [...]
        }
    """

    docs = retriever.invoke(query)

    if not docs:
        return {
            "answer": "Not found in the provided documents.",
            "sources": []
        }

    def score(doc):
        text = doc.page_content.lower()

        score = 0

        for word in query.lower().split():
            if word in text:
                score += 2

        score += min(len(text) / 200, 5)

        return score

    docs = sorted(docs, key=score, reverse=True)

    docs = docs[:4]

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are an expert AI assistant.

Answer ONLY using the provided context.

Rules:
- If the answer is not found, reply:
  "I couldn't find that information in the provided documents."
- If multiple sources mention the same thing, combine them.
- Keep the answer clear and well structured.
- Do not hallucinate.
- Do not mention that you are an AI model.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    sources = []

    seen = set()

    for doc in docs:

        metadata = doc.metadata

        key = tuple(sorted(metadata.items()))

        if key not in seen:
            seen.add(key)
            sources.append(metadata)

    return {
        "answer": response.content,
        "sources": sources
    }