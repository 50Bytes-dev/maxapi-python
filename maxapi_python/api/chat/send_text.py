from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.send_text_body import SendTextBody
from ...models.send_text_response import SendTextResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SendTextBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/send/text",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SendTextResponse]]:
    if response.status_code == 200:
        response_200 = SendTextResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, SendTextResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SendTextBody,
) -> Response[Union[ErrorResponse, SendTextResponse]]:
    """Send a text message

     Sends a text from the account to a chat, or to a person by phone. Every
    error carries a delivery outcome `code`: only `send_failed` (500) means
    the message may have arrived; every other error means nothing was sent.
    The checks run in this order: session, body, target, pause, lookup
    (cache, then MAX), send. Answers within ~9.5 s (lookup at most 4 s, the
    send's acknowledgement at most 5 s).

    A phone lookup's answer is cached per account: a found contact for 90
    days, MAX's `not.found` for 30 days. A MAX error on the lookup or the
    send whose code contains `restricted`, `limit`, `too.many`, `flood` or
    `spam` pauses the MAX account (`paused`, `pauseReason`); while paused
    every send of every gateway account of it answers 422 `send_rejected`
    without a MAX call, until `POST /session/resume`.

    Args:
        body (SendTextBody): One of `chatId` and `phone` is required; with both, `chatId` wins.
            Unknown fields are ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SendTextResponse]]
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
    body: SendTextBody,
) -> Optional[Union[ErrorResponse, SendTextResponse]]:
    """Send a text message

     Sends a text from the account to a chat, or to a person by phone. Every
    error carries a delivery outcome `code`: only `send_failed` (500) means
    the message may have arrived; every other error means nothing was sent.
    The checks run in this order: session, body, target, pause, lookup
    (cache, then MAX), send. Answers within ~9.5 s (lookup at most 4 s, the
    send's acknowledgement at most 5 s).

    A phone lookup's answer is cached per account: a found contact for 90
    days, MAX's `not.found` for 30 days. A MAX error on the lookup or the
    send whose code contains `restricted`, `limit`, `too.many`, `flood` or
    `spam` pauses the MAX account (`paused`, `pauseReason`); while paused
    every send of every gateway account of it answers 422 `send_rejected`
    without a MAX call, until `POST /session/resume`.

    Args:
        body (SendTextBody): One of `chatId` and `phone` is required; with both, `chatId` wins.
            Unknown fields are ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SendTextResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SendTextBody,
) -> Response[Union[ErrorResponse, SendTextResponse]]:
    """Send a text message

     Sends a text from the account to a chat, or to a person by phone. Every
    error carries a delivery outcome `code`: only `send_failed` (500) means
    the message may have arrived; every other error means nothing was sent.
    The checks run in this order: session, body, target, pause, lookup
    (cache, then MAX), send. Answers within ~9.5 s (lookup at most 4 s, the
    send's acknowledgement at most 5 s).

    A phone lookup's answer is cached per account: a found contact for 90
    days, MAX's `not.found` for 30 days. A MAX error on the lookup or the
    send whose code contains `restricted`, `limit`, `too.many`, `flood` or
    `spam` pauses the MAX account (`paused`, `pauseReason`); while paused
    every send of every gateway account of it answers 422 `send_rejected`
    without a MAX call, until `POST /session/resume`.

    Args:
        body (SendTextBody): One of `chatId` and `phone` is required; with both, `chatId` wins.
            Unknown fields are ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SendTextResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SendTextBody,
) -> Optional[Union[ErrorResponse, SendTextResponse]]:
    """Send a text message

     Sends a text from the account to a chat, or to a person by phone. Every
    error carries a delivery outcome `code`: only `send_failed` (500) means
    the message may have arrived; every other error means nothing was sent.
    The checks run in this order: session, body, target, pause, lookup
    (cache, then MAX), send. Answers within ~9.5 s (lookup at most 4 s, the
    send's acknowledgement at most 5 s).

    A phone lookup's answer is cached per account: a found contact for 90
    days, MAX's `not.found` for 30 days. A MAX error on the lookup or the
    send whose code contains `restricted`, `limit`, `too.many`, `flood` or
    `spam` pauses the MAX account (`paused`, `pauseReason`); while paused
    every send of every gateway account of it answers 422 `send_rejected`
    without a MAX call, until `POST /session/resume`.

    Args:
        body (SendTextBody): One of `chatId` and `phone` is required; with both, `chatId` wins.
            Unknown fields are ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SendTextResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
