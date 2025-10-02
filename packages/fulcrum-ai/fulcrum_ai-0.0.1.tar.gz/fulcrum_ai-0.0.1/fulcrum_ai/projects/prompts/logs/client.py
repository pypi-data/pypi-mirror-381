import aiohttp

from fulcrum_ai.modules.config.constants import BASE_URL

from fulcrum_ai.modules.interfaces.endpoints import (
    CreateLogRequest,
    CreateLiveLogRequest,
    CreateLiveLogResponse,
    UpdateLogRequest
)


class AsyncPromptLogsClient:

    def __init__(
        self,
        headers:dict
    ):
        self.headers = headers

    async def create_log(
        self,
        body:CreateLogRequest
    ):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{BASE_URL}/projects/prompts/logs/create/",
                headers=self.headers,
                json=body.model_dump()
            ) as response:
                if response.status != 200:
                    detail = await response.text()
                    raise Exception(
                        f"Error creating log: {response.status} {detail}"
                    )
    

    async def create_live_log(
        self,
        body:CreateLiveLogRequest
    ) -> CreateLiveLogResponse:
                        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{BASE_URL}/projects/prompts/logs/create/live",
                headers=self.headers,
                json=body.model_dump()
            ) as response:
                if response.status != 200:
                    detail = await response.text()
                    raise Exception(
                        f"Error creating live log: {response.status} {detail}"
                    )
                else:
                    return CreateLiveLogResponse(
                        **(await response.json())
                    )
    
    async def update_live_log(
        self,
        log_id:str,
        body:UpdateLogRequest
    ):
        async with aiohttp.ClientSession() as session:
            async with session.patch(
                f"{BASE_URL}/projects/prompts/logs/update/{log_id}",
                headers=self.headers,
                json=body.model_dump()
            ) as response:
                if response.status != 200:
                    detail = await response.text()
                    raise Exception(
                        f"Error updating live log: {response.status} {detail}"
                    )