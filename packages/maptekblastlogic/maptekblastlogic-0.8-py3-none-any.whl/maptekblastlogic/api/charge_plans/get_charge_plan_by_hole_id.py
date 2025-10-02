from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charge_plan_model import ChargePlanModel
from ...models.error_model import ErrorModel
from ...types import Response


def _get_kwargs(
    site_code: str,
    hole_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/site/{site_code}/hole/{hole_id}/chargePlan",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChargePlanModel, ErrorModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChargePlanModel.from_dict(response.json())

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
) -> Response[Union[ChargePlanModel, ErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_code: str,
    hole_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ChargePlanModel, ErrorModel]]:
    """Get the charge plan for a hole.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        hole_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChargePlanModel, ErrorModel]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        hole_id=hole_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_code: str,
    hole_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ChargePlanModel, ErrorModel]]:
    """Get the charge plan for a hole.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        hole_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChargePlanModel, ErrorModel]
    """

    return sync_detailed(
        site_code=site_code,
        hole_id=hole_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_code: str,
    hole_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ChargePlanModel, ErrorModel]]:
    """Get the charge plan for a hole.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        hole_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChargePlanModel, ErrorModel]]
    """

    kwargs = _get_kwargs(
        site_code=site_code,
        hole_id=hole_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_code: str,
    hole_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ChargePlanModel, ErrorModel]]:
    """Get the charge plan for a hole.

     Requires permissions:  View Blasts

    Args:
        site_code (str):
        hole_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChargePlanModel, ErrorModel]
    """

    return (
        await asyncio_detailed(
            site_code=site_code,
            hole_id=hole_id,
            client=client,
        )
    ).parsed
