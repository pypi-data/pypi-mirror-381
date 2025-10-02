from pydantic import BaseModel, Field
from typing import Optional

from ....prompts.prompt_settings.prompt_settings import (
    Providers
)

from .input_tokens import ( 
    InputTokens
)
from .output_tokens import (
    OutputTokens
)


class TotalTokens(BaseModel):
    total_tokens: int = Field(
        ...,
        description = """
            The total number of tokens involved
            in this request.
        """
    )
    total_input_tokens: int = Field(
        ...,
        description = """
            The total number of tokens used for the input/prompt.
        """
    )
    total_output_tokens: int = Field(
        ...,
        description = """
            The total number of tokens used for the output/completion.
        """
    )


class TokenDetails(BaseModel):
    
    total_tokens_object: TotalTokens = Field(
        ...,
        description = """
            The total number of tokens involved
            in this request.
        """
    )

    input_tokens_object: InputTokens = Field(
        ...,
        description = """
            A full description of the 
            input tokens used for this request.
        """
    )
    output_tokens_object: OutputTokens = Field(
        ...,
        description = """
            A full description of the 
            output tokens used for this request.
        """
    )
    
    provider: Providers = Field(
        ...,
        description="""
            Which LLM provider generated 
            this token usage
        """
    )
    
    raw_provider_token_output: Optional[dict] = Field(
        default=None,
        description="""
            Raw usage data from the 
            provider for debugging.
        """
    )