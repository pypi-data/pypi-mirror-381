from pydantic import (
    BaseModel, 
    Field
)
from typing import Optional

from fulcrum_ai.modules.interfaces.endpoints.types import (
    PromptSettings
)

class getPromptResponse(BaseModel):
    prompt_id: str
    version_id: str
    prompt: str = Field(
        description="""
            The text prompt.
        """
    )
    prompt_name: str
    prompt_description: Optional[str] = Field(
        default = None
    )

    prompt_settings: PromptSettings = Field(
        description="""
            The settings to use for the prompt.
        """
    )
