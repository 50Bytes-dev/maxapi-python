from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.user_detail import UserDetail
from ...types import Response


def _get_kwargs(
    userid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/admin/users/{userid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UserDetail]]:
    if response.status_code == 200:
        response_200 = UserDetail.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UserDetail]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, UserDetail]]:
    """Get an account

     One account with its settings. The MAX auth token is never shown, only
    whether one is stored (`auth_configured`); S3 keys are omitted and the
    proxy password is masked. The body is the account itself, without
    `success` or `data`.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UserDetail]]
    """

    kwargs = _get_kwargs(
        userid=userid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, UserDetail]]:
    """Get an account

     One account with its settings. The MAX auth token is never shown, only
    whether one is stored (`auth_configured`); S3 keys are omitted and the
    proxy password is masked. The body is the account itself, without
    `success` or `data`.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UserDetail]
    """

    return sync_detailed(
        userid=userid,
        client=client,
    ).parsed


async def asyncio_detailed(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, UserDetail]]:
    """Get an account

     One account with its settings. The MAX auth token is never shown, only
    whether one is stored (`auth_configured`); S3 keys are omitted and the
    proxy password is masked. The body is the account itself, without
    `success` or `data`.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UserDetail]]
    """

    kwargs = _get_kwargs(
        userid=userid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, UserDetail]]:
    """Get an account

     One account with its settings. The MAX auth token is never shown, only
    whether one is stored (`auth_configured`); S3 keys are omitted and the
    proxy password is masked. The body is the account itself, without
    `success` or `data`.

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UserDetail]
    """

    return (
        await asyncio_detailed(
            userid=userid,
            client=client,
        )
    ).parsed
