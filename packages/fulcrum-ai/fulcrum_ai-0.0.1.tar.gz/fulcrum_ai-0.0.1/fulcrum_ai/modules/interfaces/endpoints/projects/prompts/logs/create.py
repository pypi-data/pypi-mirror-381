from pydantic import (
    BaseModel,
    Field
)
from typing import Optional

from fulcrum_ai.modules.interfaces.endpoints.types import (
    LLMMessage,
    TokenDetails
)

class CreateLogRequest(BaseModel):
    prompt_id:str = Field(...)
    version_id:Optional[str] = Field(
        default=None,
        description="""
            The version ID of the prompt.
        """
    )

    messages:list[LLMMessage] = Field(
        ...,
        description="""
            The conversation that emerged
        """
    )

    token_details:Optional[TokenDetails] = Field(
        default=None,
        description="""
            The token details for the operation.
        """
    )

    extra_info:Optional[dict] = Field(
        default=None,
        description="""
            Any extra info that the user        
            wishes to provide about the log.
        """
    )

    task_achieved:Optional[bool] = Field(
        default=None,
        description="""
            Whether the agent self-determined
            that the task was achieved.
        """
    )


class CreateLiveLogRequest(CreateLogRequest):
    is_live:bool = Field(
        default=True,
        description="""
            Whether the log is live and actively 
            accepting updates.
        """
    )


class CreateLiveLogResponse(BaseModel):
    log_id:str = Field(
        ...,
        description="""
            The ID of the log that was created.
            You must send this back with all
            live log updates.
        """
    )
