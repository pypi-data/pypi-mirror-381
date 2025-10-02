from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_payload import ErrorResponsePayload
from ...models.notebooks_resource_folder_payload import NotebooksResourceFolderPayload
from ...models.resources_files_list_response import ResourcesFilesListResponse
from ...types import Response


def _get_kwargs(
    organisation_group: str,
    organisation_id: UUID,
    notebook_name: str,
    *,
    body: NotebooksResourceFolderPayload,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/{organisation_group}/{organisation_id}/notebooks/resource-files/{notebook_name}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponsePayload, ResourcesFilesListResponse]]:
    if response.status_code == 200:
        response_200 = ResourcesFilesListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponsePayload.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponsePayload, ResourcesFilesListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organisation_group: str,
    organisation_id: UUID,
    notebook_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotebooksResourceFolderPayload,
) -> Response[Union[ErrorResponsePayload, ResourcesFilesListResponse]]:
    """
    Args:
        organisation_group (str):
        organisation_id (UUID):
        notebook_name (str):
        body (NotebooksResourceFolderPayload):  Example: {'folderPath':
            '/metadata/metadata.json'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponsePayload, ResourcesFilesListResponse]]
    """

    kwargs = _get_kwargs(
        organisation_group=organisation_group,
        organisation_id=organisation_id,
        notebook_name=notebook_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organisation_group: str,
    organisation_id: UUID,
    notebook_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotebooksResourceFolderPayload,
) -> Optional[Union[ErrorResponsePayload, ResourcesFilesListResponse]]:
    """
    Args:
        organisation_group (str):
        organisation_id (UUID):
        notebook_name (str):
        body (NotebooksResourceFolderPayload):  Example: {'folderPath':
            '/metadata/metadata.json'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponsePayload, ResourcesFilesListResponse]
    """

    return sync_detailed(
        organisation_group=organisation_group,
        organisation_id=organisation_id,
        notebook_name=notebook_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organisation_group: str,
    organisation_id: UUID,
    notebook_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotebooksResourceFolderPayload,
) -> Response[Union[ErrorResponsePayload, ResourcesFilesListResponse]]:
    """
    Args:
        organisation_group (str):
        organisation_id (UUID):
        notebook_name (str):
        body (NotebooksResourceFolderPayload):  Example: {'folderPath':
            '/metadata/metadata.json'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponsePayload, ResourcesFilesListResponse]]
    """

    kwargs = _get_kwargs(
        organisation_group=organisation_group,
        organisation_id=organisation_id,
        notebook_name=notebook_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organisation_group: str,
    organisation_id: UUID,
    notebook_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotebooksResourceFolderPayload,
) -> Optional[Union[ErrorResponsePayload, ResourcesFilesListResponse]]:
    """
    Args:
        organisation_group (str):
        organisation_id (UUID):
        notebook_name (str):
        body (NotebooksResourceFolderPayload):  Example: {'folderPath':
            '/metadata/metadata.json'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponsePayload, ResourcesFilesListResponse]
    """

    return (
        await asyncio_detailed(
            organisation_group=organisation_group,
            organisation_id=organisation_id,
            notebook_name=notebook_name,
            client=client,
            body=body,
        )
    ).parsed
