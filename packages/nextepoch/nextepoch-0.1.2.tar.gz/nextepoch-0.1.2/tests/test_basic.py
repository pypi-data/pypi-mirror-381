import pytest

from nextepoch import MycoClient


@pytest.mark.asyncio
async def test_client_init_only():
    client = MycoClient(
        client_id="id", client_secret="secret", base_url="https://example.com/api/v1"
    )
    assert client is not None
