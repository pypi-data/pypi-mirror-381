from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dipping_entry_model import DippingEntryModel
from ...models.error_model import ErrorModel
from ...types import Response


def _get_kwargs(
    site_code: str,
    *,
    body: List["DippingEntryModel"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/site/{site_code}/dippingEntriesBulk",
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorModel, List[int]]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(List[int], response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = ErrorModel.from_dict(response.json())

        return response_413
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
) -> Response[Union[ErrorModel, List[int]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_code: str,
    *,
    client: AuthenticatedClient,
    body: List["DippingEntryModel"],
) -> Response[Union[ErrorModel, List[int]]]:
    """Create new dipping entries.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        body (List['DippingEntryModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, List[int]]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_code: str,
    *,
    client: AuthenticatedClient,
    body: List["DippingEntryModel"],
) -> Optional[Union[ErrorModel, List[int]]]:
    """Create new dipping entries.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        body (List['DippingEntryModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, List[int]]
    """

    return sync_detailed(
        site_code=site_code,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    site_code: str,
    *,
    client: AuthenticatedClient,
    body: List["DippingEntryModel"],
) -> Response[Union[ErrorModel, List[int]]]:
    """Create new dipping entries.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        body (List['DippingEntryModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, List[int]]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_code: str,
    *,
    client: AuthenticatedClient,
    body: List["DippingEntryModel"],
) -> Optional[Union[ErrorModel, List[int]]]:
    """Create new dipping entries.

     Requires permissions:  Edit Entries

    Args:
        site_code (str):
        body (List['DippingEntryModel']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, List[int]]
    """

    return (
        await asyncio_detailed(
            site_code=site_code,
            client=client,
            body=body,
        )
    ).parsed
