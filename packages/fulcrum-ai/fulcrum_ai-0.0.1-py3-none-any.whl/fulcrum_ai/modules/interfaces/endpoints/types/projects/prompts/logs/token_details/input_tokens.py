from pydantic import BaseModel, Field
from typing import Optional


    
class InputTokens(BaseModel):
    cached_text_input_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of text input 
            tokens read from cache.
        """
    )
    new_text_input_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of text input 
            tokens that were not read 
            from cache.
        """
    )
    cached_image_input_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of image input 
            tokens read from cache.
        """
    )
    new_image_input_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of image input 
            tokens that were not read 
            from cache.
        """
    )
    cached_audio_input_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of audio input 
            tokens read from cache.
        """
    )
    new_audio_input_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of audio input 
            tokens that were not read 
            from cache.
        """
    )
    cache_creation_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of tokens used to 
            create new cache entries for
            future requests.
        """
    )