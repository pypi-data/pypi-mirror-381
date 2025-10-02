from pydantic import BaseModel, Field
from typing import Optional


class OutputTokens(BaseModel):
    output_text_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of text output 
            tokens read from cache.
        """
    )
    reasoning_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of tokens used for reasoning.
        """
    )
    output_image_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of image output 
            tokens read from cache.
        """
    )
    output_audio_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of audio output 
            tokens read from cache.
        """
    )

    accepted_prediction_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of tokens used 
            that were accepted and used in
            the final output.
        """
    )
    rejected_prediction_tokens: Optional[int] = Field(
        default = None,
        description = """
            The number of tokens that were
            rejected and not used in the
            final output.
        """
    )
