from pydantic import (
    BaseModel, 
    Field
)
from enum import Enum
from typing import Optional


class Models(str, Enum):
    gpt_5 = "gpt-5"
    gpt_4o = "gpt-4o"
    o3_mini = "o3-mini"

    claude_4_sonnet = "claude-4-sonnet"

class Providers(str, Enum):
    openai = "openai"
    anthropic = "anthropic"

MODEL_PROVIDER_MAP: dict[
    Providers, 
    list[Models]
] = {
    Providers.openai: [
        Models.gpt_5, 
        Models.o3_mini, 
        Models.gpt_4o
    ],
    Providers.anthropic: [Models.claude_4_sonnet],
}

class ResponseFormats(str, Enum):
    text = "text"
    json_object = "json_object"
    json_schema = "json_schema"

class PromptSettings(BaseModel):
    provider:Providers = Field(
        default=Providers.openai,
        description="""
            The provider to use for the prompt.
        """
    )

    model:str = Field(
        default=Models.gpt_5,
        description="""
            The model to use for the prompt.
        """
    )

    max_tokens:Optional[int] = Field(
        default=None,
        description="""
            The maximum number of tokens to use for the prompt.
        """
    )

    temperature:float = Field(
        default=0.7,
        description="""
            The temperature to use for the prompt.
        """
    )
    response_format:ResponseFormats = Field(
        default=ResponseFormats.text,
        description="""
            The response format to use for the prompt.
        """
    )