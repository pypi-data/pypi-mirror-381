from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dipping_entry_model import DippingEntryModel
from ...models.error_model import ErrorModel
from ...types import Response


def _get_kwargs(
    site_code: str,
    dipping_entry_id: int,
    *,
    body: DippingEntryModel,
    if_match: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["If-Match"] = if_match

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/site/{site_code}/dippingEntry/{dipping_entry_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorModel]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorModel.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorModel.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorModel.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ErrorModel.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_code: str,
    dipping_entry_id: int,
    *,
    client: AuthenticatedClient,
    body: DippingEntryModel,
    if_match: str,
) -> Response[Union[Any, ErrorModel]]:
    """Update an existing dipping entry.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        dipping_entry_id (int):
        if_match (str):
        body (DippingEntryModel): Details of a dipping activity on a hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        dipping_entry_id=dipping_entry_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_code: str,
    dipping_entry_id: int,
    *,
    client: AuthenticatedClient,
    body: DippingEntryModel,
    if_match: str,
) -> Optional[Union[Any, ErrorModel]]:
    """Update an existing dipping entry.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        dipping_entry_id (int):
        if_match (str):
        body (DippingEntryModel): Details of a dipping activity on a hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel]
    """

    return sync_detailed(
        site_code=site_code,
        dipping_entry_id=dipping_entry_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    site_code: str,
    dipping_entry_id: int,
    *,
    client: AuthenticatedClient,
    body: DippingEntryModel,
    if_match: str,
) -> Response[Union[Any, ErrorModel]]:
    """Update an existing dipping entry.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        dipping_entry_id (int):
        if_match (str):
        body (DippingEntryModel): Details of a dipping activity on a hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorModel]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        dipping_entry_id=dipping_entry_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_code: str,
    dipping_entry_id: int,
    *,
    client: AuthenticatedClient,
    body: DippingEntryModel,
    if_match: str,
) -> Optional[Union[Any, ErrorModel]]:
    """Update an existing dipping entry.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        dipping_entry_id (int):
        if_match (str):
        body (DippingEntryModel): Details of a dipping activity on a hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorModel]
    """

    return (
        await asyncio_detailed(
            site_code=site_code,
            dipping_entry_id=dipping_entry_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
