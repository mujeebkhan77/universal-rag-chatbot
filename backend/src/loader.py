from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    """Fetch transcript from a YouTube video
    and return it as one string."""
    
    transcript = YouTubeTranscriptApi().fetch(video_id)
    text = " ".join([item.text for item in transcript])
    
    return text

    
    
