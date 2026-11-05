from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.send_audio_body import SendAudioBody
from ...models.send_text_response import SendTextResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SendAudioBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/send/audio",
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

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

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
    body: SendAudioBody,
) -> Response[Union[ErrorResponse, SendTextResponse]]:
    """Send an audio file

     Sends an audio file, sent as a file: the media is fetched or decoded (a URL goes through the
    SSRF guard, at most `MAXAPI_MEDIA_MAX_BYTES`), uploaded to MAX, then
    sent with the rules and codes of `POST /chat/send/text`: the pause, the
    phone lookup through the cache, `ref`. The checks run in this order:
    session, body, target, caption, pause, media, upload, lookup, send.
    MAX refusing the upload, or the upload failing, answers 422
    `attachment_rejected`. The upload takes up to ~90 s for a document
    or audio and ~270 s for a video (the upload address, the upload, MAX's
    processing) on top of the send's ~9.5 s.

    Args:
        body (SendAudioBody):

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
    body: SendAudioBody,
) -> Optional[Union[ErrorResponse, SendTextResponse]]:
    """Send an audio file

     Sends an audio file, sent as a file: the media is fetched or decoded (a URL goes through the
    SSRF guard, at most `MAXAPI_MEDIA_MAX_BYTES`), uploaded to MAX, then
    sent with the rules and codes of `POST /chat/send/text`: the pause, the
    phone lookup through the cache, `ref`. The checks run in this order:
    session, body, target, caption, pause, media, upload, lookup, send.
    MAX refusing the upload, or the upload failing, answers 422
    `attachment_rejected`. The upload takes up to ~90 s for a document
    or audio and ~270 s for a video (the upload address, the upload, MAX's
    processing) on top of the send's ~9.5 s.

    Args:
        body (SendAudioBody):

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
    body: SendAudioBody,
) -> Response[Union[ErrorResponse, SendTextResponse]]:
    """Send an audio file

     Sends an audio file, sent as a file: the media is fetched or decoded (a URL goes through the
    SSRF guard, at most `MAXAPI_MEDIA_MAX_BYTES`), uploaded to MAX, then
    sent with the rules and codes of `POST /chat/send/text`: the pause, the
    phone lookup through the cache, `ref`. The checks run in this order:
    session, body, target, caption, pause, media, upload, lookup, send.
    MAX refusing the upload, or the upload failing, answers 422
    `attachment_rejected`. The upload takes up to ~90 s for a document
    or audio and ~270 s for a video (the upload address, the upload, MAX's
    processing) on top of the send's ~9.5 s.

    Args:
        body (SendAudioBody):

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
    body: SendAudioBody,
) -> Optional[Union[ErrorResponse, SendTextResponse]]:
    """Send an audio file

     Sends an audio file, sent as a file: the media is fetched or decoded (a URL goes through the
    SSRF guard, at most `MAXAPI_MEDIA_MAX_BYTES`), uploaded to MAX, then
    sent with the rules and codes of `POST /chat/send/text`: the pause, the
    phone lookup through the cache, `ref`. The checks run in this order:
    session, body, target, caption, pause, media, upload, lookup, send.
    MAX refusing the upload, or the upload failing, answers 422
    `attachment_rejected`. The upload takes up to ~90 s for a document
    or audio and ~270 s for a video (the upload address, the upload, MAX's
    processing) on top of the send's ~9.5 s.

    Args:
        body (SendAudioBody):

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
