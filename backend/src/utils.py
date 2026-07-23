from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str):
    """
    Extract YouTube video ID from different URL formats.
    """

    parsed = urlparse(url)

    hostname = parsed.hostname

    if hostname == "youtu.be":
        return parsed.path.lstrip("/")


    if hostname and "youtube.com" in hostname:

        # normal video
        if "v" in parse_qs(parsed.query):
            return parse_qs(parsed.query)["v"][0]

        # shorts
        if "/shorts/" in parsed.path:
            return parsed.path.split("/shorts/")[1]


    return None