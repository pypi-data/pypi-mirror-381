from .content_media import ChattyContentMedia
from pydantic import Field
from typing import Optional

class ChattyContentAudio(ChattyContentMedia):
    transcript: Optional[str] = Field(default=None, description="The transcript of the audio")