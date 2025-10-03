from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_write_request import FileWriteRequest
from ...models.fs_write_v1_computer_machine_id_fs_write_post_response_fs_write_v1_computer_machine_id_fs_write_post import (
    FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    machine_id: str,
    *,
    body: FileWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/computer/{machine_id}/fs/write",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
]:
    if response.status_code == 200:
        response_200 = FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost.from_dict(
            response.json()
        )

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
) -> Response[
    Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    machine_id: str,
    *,
    client: AuthenticatedClient,
    body: FileWriteRequest,
) -> Response[
    Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
]:
    """Write file contents

     Write file contents to the machine.

    Args:
        machine_id (str):
        body (FileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    machine_id: str,
    *,
    client: AuthenticatedClient,
    body: FileWriteRequest,
) -> Optional[
    Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
]:
    """Write file contents

     Write file contents to the machine.

    Args:
        machine_id (str):
        body (FileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
    """

    return sync_detailed(
        machine_id=machine_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    machine_id: str,
    *,
    client: AuthenticatedClient,
    body: FileWriteRequest,
) -> Response[
    Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
]:
    """Write file contents

     Write file contents to the machine.

    Args:
        machine_id (str):
        body (FileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    machine_id: str,
    *,
    client: AuthenticatedClient,
    body: FileWriteRequest,
) -> Optional[
    Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
]:
    """Write file contents

     Write file contents to the machine.

    Args:
        machine_id (str):
        body (FileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FsWriteV1ComputerMachineIdFsWritePostResponseFsWriteV1ComputerMachineIdFsWritePost, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            machine_id=machine_id,
            client=client,
            body=body,
        )
    ).parsed
