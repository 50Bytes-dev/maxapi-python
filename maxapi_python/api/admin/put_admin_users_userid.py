from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_user_body import EditUserBody
from ...models.error_response import ErrorResponse
from ...models.message_response import MessageResponse
from ...types import Response


def _get_kwargs(
    userid: str,
    *,
    body: EditUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/admin/users/{userid}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, MessageResponse]]:
    if response.status_code == 200:
        response_200 = MessageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, MessageResponse]]:
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
    body: EditUserBody,
) -> Response[Union[ErrorResponse, MessageResponse]]:
    """Update user

     Updates an existing user

    Args:
        userid (str):
        body (EditUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MessageResponse]]
    """

    kwargs = _get_kwargs(
        userid=userid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    userid: str,
    *,
    client: AuthenticatedClient,
    body: EditUserBody,
) -> Optional[Union[ErrorResponse, MessageResponse]]:
    """Update user

     Updates an existing user

    Args:
        userid (str):
        body (EditUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, MessageResponse]
    """

    return sync_detailed(
        userid=userid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    userid: str,
    *,
    client: AuthenticatedClient,
    body: EditUserBody,
) -> Response[Union[ErrorResponse, MessageResponse]]:
    """Update user

     Updates an existing user

    Args:
        userid (str):
        body (EditUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MessageResponse]]
    """

    kwargs = _get_kwargs(
        userid=userid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    userid: str,
    *,
    client: AuthenticatedClient,
    body: EditUserBody,
) -> Optional[Union[ErrorResponse, MessageResponse]]:
    """Update user

     Updates an existing user

    Args:
        userid (str):
        body (EditUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, MessageResponse]
    """

    return (
        await asyncio_detailed(
            userid=userid,
            client=client,
            body=body,
        )
    ).parsed
