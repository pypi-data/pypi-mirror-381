from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_status import ConnectionStatus
from ...models.http_validation_error import HTTPValidationError
from ...models.paginated_response_connection_response import PaginatedResponseConnectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    machine_id: Union[None, UUID, Unset] = UNSET,
    status: Union[ConnectionStatus, None, Unset] = UNSET,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_machine_id: Union[None, Unset, str]
    if isinstance(machine_id, Unset):
        json_machine_id = UNSET
    elif isinstance(machine_id, UUID):
        json_machine_id = str(machine_id)
    else:
        json_machine_id = machine_id
    params["machine_id"] = json_machine_id

    json_status: Union[None, Unset, str]
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ConnectionStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedResponseConnectionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    machine_id: Union[None, UUID, Unset] = UNSET,
    status: Union[ConnectionStatus, None, Unset] = UNSET,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Response[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]:
    """List Connections

     List all connections for the authenticated organization's machines.

    Supports pagination and filtering by machine and status.
    Returns connections with their associated machine data.

    Args:
        machine_id (Union[None, UUID, Unset]): Filter by machine ID
        status (Union[ConnectionStatus, None, Unset]): Filter by connection status
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        status=status,
        skip=skip,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    machine_id: Union[None, UUID, Unset] = UNSET,
    status: Union[ConnectionStatus, None, Unset] = UNSET,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]:
    """List Connections

     List all connections for the authenticated organization's machines.

    Supports pagination and filtering by machine and status.
    Returns connections with their associated machine data.

    Args:
        machine_id (Union[None, UUID, Unset]): Filter by machine ID
        status (Union[ConnectionStatus, None, Unset]): Filter by connection status
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginatedResponseConnectionResponse]
    """

    return sync_detailed(
        client=client,
        machine_id=machine_id,
        status=status,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    machine_id: Union[None, UUID, Unset] = UNSET,
    status: Union[ConnectionStatus, None, Unset] = UNSET,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Response[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]:
    """List Connections

     List all connections for the authenticated organization's machines.

    Supports pagination and filtering by machine and status.
    Returns connections with their associated machine data.

    Args:
        machine_id (Union[None, UUID, Unset]): Filter by machine ID
        status (Union[ConnectionStatus, None, Unset]): Filter by connection status
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        status=status,
        skip=skip,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    machine_id: Union[None, UUID, Unset] = UNSET,
    status: Union[ConnectionStatus, None, Unset] = UNSET,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[HTTPValidationError, PaginatedResponseConnectionResponse]]:
    """List Connections

     List all connections for the authenticated organization's machines.

    Supports pagination and filtering by machine and status.
    Returns connections with their associated machine data.

    Args:
        machine_id (Union[None, UUID, Unset]): Filter by machine ID
        status (Union[ConnectionStatus, None, Unset]): Filter by connection status
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PaginatedResponseConnectionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            machine_id=machine_id,
            status=status,
            skip=skip,
            limit=limit,
        )
    ).parsed
