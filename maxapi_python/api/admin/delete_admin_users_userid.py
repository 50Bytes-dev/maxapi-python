from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data import Data
from ...types import Response


def _get_kwargs(
    userid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/admin/users/{userid}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Data]:
    if response.status_code == 200:
        response_200 = Data.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = Data.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Data]:
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
) -> Response[Data]:
    """Delete user

     Deletes a user from the system

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Data]
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
) -> Optional[Data]:
    """Delete user

     Deletes a user from the system

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Data
    """

    return sync_detailed(
        userid=userid,
        client=client,
    ).parsed


async def asyncio_detailed(
    userid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Data]:
    """Delete user

     Deletes a user from the system

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Data]
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
) -> Optional[Data]:
    """Delete user

     Deletes a user from the system

    Args:
        userid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Data
    """

    return (
        await asyncio_detailed(
            userid=userid,
            client=client,
        )
    ).parsed
