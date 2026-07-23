from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document
import uuid

def load_youtube_transcript(video_id: str):
    """
    Extract transcript from YouTube video.
    """

    transcript = YouTubeTranscriptApi().fetch(video_id)

    text = " ".join(
        [
            item.text.replace("\n", " ")
            for item in transcript
        ]
    )

    document = Document(
        page_content=text,
        metadata={
            "document_id" : str(uuid.uuid4()),
            "source": "youtube",
            "file": video_id,
            "video_id": video_id
        }
    )

    return [document]