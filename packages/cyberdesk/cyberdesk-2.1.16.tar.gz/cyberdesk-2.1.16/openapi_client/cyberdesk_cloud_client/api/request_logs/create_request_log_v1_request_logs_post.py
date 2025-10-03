from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.request_log_create import RequestLogCreate
from ...models.request_log_response import RequestLogResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RequestLogCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/request-logs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, RequestLogResponse]]:
    if response.status_code == 201:
        response_201 = RequestLogResponse.from_dict(response.json())

        return response_201
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, RequestLogResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestLogCreate,
) -> Response[Union[HTTPValidationError, RequestLogResponse]]:
    """Create Request Log

     Create a new request log.

    The machine must exist and belong to the authenticated organization.
    This is typically called when a request is initiated.

    Args:
        body (RequestLogCreate): Schema for creating a request log

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RequestLogResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RequestLogCreate,
) -> Optional[Union[HTTPValidationError, RequestLogResponse]]:
    """Create Request Log

     Create a new request log.

    The machine must exist and belong to the authenticated organization.
    This is typically called when a request is initiated.

    Args:
        body (RequestLogCreate): Schema for creating a request log

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RequestLogResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestLogCreate,
) -> Response[Union[HTTPValidationError, RequestLogResponse]]:
    """Create Request Log

     Create a new request log.

    The machine must exist and belong to the authenticated organization.
    This is typically called when a request is initiated.

    Args:
        body (RequestLogCreate): Schema for creating a request log

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RequestLogResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RequestLogCreate,
) -> Optional[Union[HTTPValidationError, RequestLogResponse]]:
    """Create Request Log

     Create a new request log.

    The machine must exist and belong to the authenticated organization.
    This is typically called when a request is initiated.

    Args:
        body (RequestLogCreate): Schema for creating a request log

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RequestLogResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
