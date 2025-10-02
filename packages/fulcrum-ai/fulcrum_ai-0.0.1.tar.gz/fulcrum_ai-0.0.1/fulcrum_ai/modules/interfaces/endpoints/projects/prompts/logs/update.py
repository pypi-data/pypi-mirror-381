from pydantic import (
    BaseModel,
    Field
)
from typing import Optional

from fulcrum_ai.modules.interfaces.endpoints.types import (
    LLMMessage,
    TokenDetails
)


class UpdateLogRequest(BaseModel):
    additional_messages:Optional[list[LLMMessage]] = Field(
        default=None,
        description="""
            The additional messages to add to the log.
        """
    )
    token_details:Optional[TokenDetails] = Field(
        default=None,
        description="""
            The token details for the operation.
        """
    )
    task_achieved:Optional[bool] = Field(
        default=None,
        description="""
            Whether the task was achieved.
        """
    )
    extra_info:Optional[dict] = Field(
        default=None,
        description="""
            Any extra info that the user        
            wishes to provide about the log.
        """
    )
    is_last_message:Optional[bool] = Field(
        default=False,
        description="""
            Whether the additional messages are the last
            messages in the log. If true, the log will
            be marked as completed.
        """
    )