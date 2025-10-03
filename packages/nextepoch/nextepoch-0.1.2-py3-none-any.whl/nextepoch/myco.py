from typing import Any, Dict, Optional

import aiohttp


class MycoClient:
    """
    Thin client for Myco Models API.
    """

    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        base_url: str,
        organization_id: Optional[str] = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url.rstrip("/")
        self.organization_id = organization_id

    async def extract(
        self, *, text: str, parameters: Any, required: Any, model: str = "gpt-4o-mini"
    ) -> Dict[str, Any]:
        url = f"{self.base_url}/text/extract"
        if self.organization_id:
            url += f"?organization={self.organization_id}"

        auth = aiohttp.BasicAuth(self.client_id, self.client_secret).encode()

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                headers={
                    "Authorization": f"Basic {auth}",
                    "Content-Type": "application/json",
                },
                json={
                    "text": text,
                    "parameters": parameters,
                    "required": required,
                    "model": model,
                },
            ) as resp:
                if resp.status != 200:
                    raise RuntimeError(
                        f"Myco extract failed ({resp.status}): {await resp.text()}"
                    )
                return await resp.json()
