from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.resume_body import ResumeBody
from ...models.resume_response import ResumeResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ResumeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/resume",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ResumeResponse]]:
    if response.status_code == 200:
        response_200 = ResumeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ResumeResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ResumeBody,
) -> Response[Union[ErrorResponse, ResumeResponse]]:
    """Resume sending from the account

     Lifts the pause of the MAX account this account is logged into (the
    live session's, or the one stored at the last login), for every gateway
    account logged into it; `maxUserID` names the MAX account. An account
    that is not paused, or whose MAX account is unknown, answers the same.
    Every gateway account of the MAX account subscribed to `Resumed` (or
    `All`) gets that event. The body is optional. No MAX call.

    Args:
        body (ResumeBody): Optional; no body and `{}` work too.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResumeResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ResumeBody,
) -> Optional[Union[ErrorResponse, ResumeResponse]]:
    """Resume sending from the account

     Lifts the pause of the MAX account this account is logged into (the
    live session's, or the one stored at the last login), for every gateway
    account logged into it; `maxUserID` names the MAX account. An account
    that is not paused, or whose MAX account is unknown, answers the same.
    Every gateway account of the MAX account subscribed to `Resumed` (or
    `All`) gets that event. The body is optional. No MAX call.

    Args:
        body (ResumeBody): Optional; no body and `{}` work too.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResumeResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ResumeBody,
) -> Response[Union[ErrorResponse, ResumeResponse]]:
    """Resume sending from the account

     Lifts the pause of the MAX account this account is logged into (the
    live session's, or the one stored at the last login), for every gateway
    account logged into it; `maxUserID` names the MAX account. An account
    that is not paused, or whose MAX account is unknown, answers the same.
    Every gateway account of the MAX account subscribed to `Resumed` (or
    `All`) gets that event. The body is optional. No MAX call.

    Args:
        body (ResumeBody): Optional; no body and `{}` work too.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResumeResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ResumeBody,
) -> Optional[Union[ErrorResponse, ResumeResponse]]:
    """Resume sending from the account

     Lifts the pause of the MAX account this account is logged into (the
    live session's, or the one stored at the last login), for every gateway
    account logged into it; `maxUserID` names the MAX account. An account
    that is not paused, or whose MAX account is unknown, answers the same.
    Every gateway account of the MAX account subscribed to `Resumed` (or
    `All`) gets that event. The body is optional. No MAX call.

    Args:
        body (ResumeBody): Optional; no body and `{}` work too.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResumeResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
