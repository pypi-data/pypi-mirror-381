from pydantic import BaseModel
from typing import Literal
from enum import Enum

class _ContentTypes(str, Enum):
    TEXT = "text"
    IMAGE_URL = "image_url"

# IMAGES

class ImageURL(BaseModel):
    url: str
    detail: Literal["low", "high", "auto"] = "auto"

class _ImageContent(BaseModel):
    type: Literal[_ContentTypes.IMAGE_URL]
    image_url: ImageURL 




# TEXT
class _TextContent(BaseModel):
    type: Literal[_ContentTypes.TEXT]
    text: str


__all__ = [
    "ImageURL",
    "_ImageContent",
    "_TextContent",
    "_ContentTypes"
]