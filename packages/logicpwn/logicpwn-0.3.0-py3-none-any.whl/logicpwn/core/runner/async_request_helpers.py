"""
Async request helper functions for LogicPwn.
"""

from contextlib import asynccontextmanager
from typing import Any, Optional, Union

from logicpwn.models.request_config import RequestConfig
from logicpwn.models.request_result import RequestResult


async def send_request_async(
    url: str, method: str = "GET", headers: Optional[dict[str, str]] = None, **kwargs
) -> RequestResult:
    """
    Send a single async HTTP request.
    Args:
        url: Target URL
        method: HTTP method
        headers: Request headers
        **kwargs: Additional request parameters
    Returns:
        RequestResult with response analysis
    """
    from .async_runner_core import AsyncRequestRunner

    async with AsyncRequestRunner() as runner:
        return await runner.send_request(
            url=url, method=method, headers=headers, **kwargs
        )


async def send_requests_batch_async(
    request_configs: list[Union[dict[str, Any], RequestConfig]],
    max_concurrent: int = 10,
) -> list[RequestResult]:
    """
    Send multiple requests concurrently.
    Args:
        request_configs: List of request configurations
        max_concurrent: Maximum concurrent requests
    Returns:
        List of RequestResult objects
    """
    from .async_runner_core import AsyncRequestRunner

    async with AsyncRequestRunner(max_concurrent=max_concurrent) as runner:
        return await runner.send_requests_batch(request_configs)


@asynccontextmanager
async def async_session_manager(
    auth_config: Optional[dict[str, Any]] = None, max_concurrent: int = 10
):
    """
    Async context manager for session management.
    Args:
        auth_config: Authentication configuration
        max_concurrent: Maximum concurrent requests
    Yields:
        AsyncSessionManager instance
    """
    from .async_session_manager import AsyncSessionManager

    async with AsyncSessionManager(
        auth_config=auth_config, max_concurrent=max_concurrent
    ) as session:
        yield session
