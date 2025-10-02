from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_model import ErrorModel
from ...models.loaded_deck_model import LoadedDeckModel
from ...types import Response


def _get_kwargs(
    site_code: str,
    *,
    body: LoadedDeckModel,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/site/{site_code}/loadedDecks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorModel, int]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(int, response.json())
        return response_201
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
) -> Response[Union[ErrorModel, int]]:
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
    body: LoadedDeckModel,
) -> Response[Union[ErrorModel, int]]:
    """Create a new Loaded Deck.

     Requires permissions:  Edit Charging Events

    Args:
        site_code (str):
        body (LoadedDeckModel): Describes the loading of an individual deck. This is raw data
            collected from the field that has not been validated and reconciled in BlastLogic Desktop.
            As such, decks may overlap with each other. This data should not be relied upon as the
            current state of the hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, int]]
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
    body: LoadedDeckModel,
) -> Optional[Union[ErrorModel, int]]:
    """Create a new Loaded Deck.

     Requires permissions:  Edit Charging Events

    Args:
        site_code (str):
        body (LoadedDeckModel): Describes the loading of an individual deck. This is raw data
            collected from the field that has not been validated and reconciled in BlastLogic Desktop.
            As such, decks may overlap with each other. This data should not be relied upon as the
            current state of the hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, int]
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
    body: LoadedDeckModel,
) -> Response[Union[ErrorModel, int]]:
    """Create a new Loaded Deck.

     Requires permissions:  Edit Charging Events

    Args:
        site_code (str):
        body (LoadedDeckModel): Describes the loading of an individual deck. This is raw data
            collected from the field that has not been validated and reconciled in BlastLogic Desktop.
            As such, decks may overlap with each other. This data should not be relied upon as the
            current state of the hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, int]]
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
    body: LoadedDeckModel,
) -> Optional[Union[ErrorModel, int]]:
    """Create a new Loaded Deck.

     Requires permissions:  Edit Charging Events

    Args:
        site_code (str):
        body (LoadedDeckModel): Describes the loading of an individual deck. This is raw data
            collected from the field that has not been validated and reconciled in BlastLogic Desktop.
            As such, decks may overlap with each other. This data should not be relied upon as the
            current state of the hole.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, int]
    """

    return (
        await asyncio_detailed(
            site_code=site_code,
            client=client,
            body=body,
        )
    ).parsed
