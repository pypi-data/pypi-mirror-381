from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from .content_types import (    
    _ImageContent,
    _TextContent
)

class LLMMessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"

_Content = _ImageContent | _TextContent


# TOOL CALLING
class ToolFunctionDetails(BaseModel):
    arguments: str
    name: str

class LLMMessageToolCall(BaseModel):
    id: str
    function: ToolFunctionDetails
    type: str

class LLMMessage(BaseModel):
    role: LLMMessageRole
    annotations: Optional[list[str]] = Field(
        default = None
    )
    content: Optional[str | list[_Content]] = Field(
        default = None
    )
    tool_calls : Optional[list[
        LLMMessageToolCall
    ]] = Field(
        default = None
    )
    tool_call_id: Optional[str] = Field(
        default = None
    )