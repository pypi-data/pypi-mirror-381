from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.product_model import ProductModel
from ...types import Response


def _get_kwargs(
    site_code: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/site/{site_code}/deckProducts",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorModel, List["ProductModel"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProductModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
) -> Response[Union[ErrorModel, List["ProductModel"]]]:
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
) -> Response[Union[ErrorModel, List["ProductModel"]]]:
    """Get all products usable in decks.

     Requires permissions: Any

    Args:
        site_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, List['ProductModel']]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_code: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorModel, List["ProductModel"]]]:
    """Get all products usable in decks.

     Requires permissions: Any

    Args:
        site_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, List['ProductModel']]
    """

    return sync_detailed(
        site_code=site_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorModel, List["ProductModel"]]]:
    """Get all products usable in decks.

     Requires permissions: Any

    Args:
        site_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, List['ProductModel']]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_code: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorModel, List["ProductModel"]]]:
    """Get all products usable in decks.

     Requires permissions: Any

    Args:
        site_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, List['ProductModel']]
    """

    return (
        await asyncio_detailed(
            site_code=site_code,
            client=client,
        )
    ).parsed
