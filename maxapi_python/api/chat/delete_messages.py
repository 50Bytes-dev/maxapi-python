from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_messages_body import DeleteMessagesBody
from ...models.delete_messages_response import DeleteMessagesResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteMessagesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteMessagesResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteMessagesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

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
) -> Response[Union[DeleteMessagesResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteMessagesBody,
) -> Response[Union[DeleteMessagesResponse, ErrorResponse]]:
    """Delete messages for everyone

     Deletes up to 100 messages of one chat for everyone, in one MAX call,
    and answers per message. MAX answers with the ids it deleted: those are
    `deleted`, the rest `not_found`. When MAX refuses the whole call with a
    code of a message (not found, too old, no right), every id gets that
    status with `upstreamCode`. The pause applies as to a send (422
    `send_rejected`), and a stop signal pauses the account. Answers within
    ~5.5 s.

    Args:
        body (DeleteMessagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteMessagesResponse, ErrorResponse]]
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
    body: DeleteMessagesBody,
) -> Optional[Union[DeleteMessagesResponse, ErrorResponse]]:
    """Delete messages for everyone

     Deletes up to 100 messages of one chat for everyone, in one MAX call,
    and answers per message. MAX answers with the ids it deleted: those are
    `deleted`, the rest `not_found`. When MAX refuses the whole call with a
    code of a message (not found, too old, no right), every id gets that
    status with `upstreamCode`. The pause applies as to a send (422
    `send_rejected`), and a stop signal pauses the account. Answers within
    ~5.5 s.

    Args:
        body (DeleteMessagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteMessagesResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteMessagesBody,
) -> Response[Union[DeleteMessagesResponse, ErrorResponse]]:
    """Delete messages for everyone

     Deletes up to 100 messages of one chat for everyone, in one MAX call,
    and answers per message. MAX answers with the ids it deleted: those are
    `deleted`, the rest `not_found`. When MAX refuses the whole call with a
    code of a message (not found, too old, no right), every id gets that
    status with `upstreamCode`. The pause applies as to a send (422
    `send_rejected`), and a stop signal pauses the account. Answers within
    ~5.5 s.

    Args:
        body (DeleteMessagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteMessagesResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DeleteMessagesBody,
) -> Optional[Union[DeleteMessagesResponse, ErrorResponse]]:
    """Delete messages for everyone

     Deletes up to 100 messages of one chat for everyone, in one MAX call,
    and answers per message. MAX answers with the ids it deleted: those are
    `deleted`, the rest `not_found`. When MAX refuses the whole call with a
    code of a message (not found, too old, no right), every id gets that
    status with `upstreamCode`. The pause applies as to a send (422
    `send_rejected`), and a stop signal pauses the account. Answers within
    ~5.5 s.

    Args:
        body (DeleteMessagesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteMessagesResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
