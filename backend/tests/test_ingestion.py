from src.ingestion import ingest


# Test YouTube
youtube_source = "7ARBJQn6QkM"

print("Processing YouTube...")

vectorstore = ingest(
    youtube_source,
    "youtube"
)

print("✅ YouTube ingestion completed")


# Test PDF
pdf_source = "sample_data/sample.pdf"

print("Processing PDF...")

vectorstore = ingest(
    pdf_source,
    "pdf"
)

print("✅ PDF ingestion completed")