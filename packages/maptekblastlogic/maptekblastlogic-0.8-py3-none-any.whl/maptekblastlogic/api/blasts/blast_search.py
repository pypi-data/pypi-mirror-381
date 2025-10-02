from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blast_model import BlastModel
from ...models.error_model import ErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_code: str,
    *,
    blast_name_pattern: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_blast_name_pattern: Union[None, Unset, str]
    if isinstance(blast_name_pattern, Unset):
        json_blast_name_pattern = UNSET
    else:
        json_blast_name_pattern = blast_name_pattern
    params["blastNamePattern"] = json_blast_name_pattern

    json_status: Union[None, Unset, str]
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/site/{site_code}/blasts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorModel, List["BlastModel"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BlastModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorModel.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorModel.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ErrorModel.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorModel, List["BlastModel"]]]:
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
    blast_name_pattern: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorModel, List["BlastModel"]]]:
    """Search for blasts by name and status.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        blast_name_pattern (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, List['BlastModel']]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        blast_name_pattern=blast_name_pattern,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_code: str,
    *,
    client: AuthenticatedClient,
    blast_name_pattern: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorModel, List["BlastModel"]]]:
    """Search for blasts by name and status.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        blast_name_pattern (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, List['BlastModel']]
    """

    return sync_detailed(
        site_code=site_code,
        client=client,
        blast_name_pattern=blast_name_pattern,
        status=status,
    ).parsed


async def asyncio_detailed(
    site_code: str,
    *,
    client: AuthenticatedClient,
    blast_name_pattern: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorModel, List["BlastModel"]]]:
    """Search for blasts by name and status.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        blast_name_pattern (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorModel, List['BlastModel']]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        blast_name_pattern=blast_name_pattern,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_code: str,
    *,
    client: AuthenticatedClient,
    blast_name_pattern: Union[None, Unset, str] = UNSET,
    status: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorModel, List["BlastModel"]]]:
    """Search for blasts by name and status.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        blast_name_pattern (Union[None, Unset, str]):
        status (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorModel, List['BlastModel']]
    """

    return (
        await asyncio_detailed(
            site_code=site_code,
            client=client,
            blast_name_pattern=blast_name_pattern,
            status=status,
        )
    ).parsed
