import requests

from .modules.config.constants import BASE_URL

from .projects.prompts import AsyncPromptClient




class AsyncFulcrumClient:

    def __init__(
        self,
        api_key:str
    ):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Test the connection
        _test_connection()

        # Test the authentication
        _test_authentication(self.headers)

        self.prompts = AsyncPromptClient(self.headers)








def _test_connection():
    try:
        requests.request(
            method="GET",
            url=f"{BASE_URL}/connect/"
        )
    except Exception as e:
        raise Exception(f"""
            Error connecting to Fulcrum AI API. 
            This is not an authentication issue.
            Exception detials:
            {e}
        """)


def _test_authentication(
    headers:dict
):
    response = requests.request(
        method="POST",
        url=f"{BASE_URL}/connect/auth-test",
        headers=headers
    )
    if response.status_code == 401:
        raise Exception(response.json()["detail"])
    