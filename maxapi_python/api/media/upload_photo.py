from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.photo_body import PhotoBody
from ...models.photo_response import PhotoResponse
from ...models.upload_photo_files_body import UploadPhotoFilesBody
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        PhotoBody,
        UploadPhotoFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/media/photo",
    }

    if isinstance(body, PhotoBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UploadPhotoFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PhotoResponse]]:
    if response.status_code == 200:
        response_200 = PhotoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, PhotoResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        PhotoBody,
        UploadPhotoFilesBody,
    ],
) -> Response[Union[ErrorResponse, PhotoResponse]]:
    """Upload a photo once

     Uploads a photo to MAX for the account and answers with its
    `attachment`, which `POST /chat/send/text` takes in `attachments` for
    any chat of the account. The photo comes as JSON `{url}` or `{data}`
    (base64 or a data URL), or as a multipart form with a `file` field. The
    body, and the photo, are at most `MAXAPI_PHOTO_MAX_BYTES` (10 MiB by
    default). A URL is fetched by the gateway through its SSRF guard (http
    and https only, no internal address, 8 s, a 2xx answer). The photo must
    be a JPEG, PNG, GIF or WebP image; `width` and `height` are read from
    it. Then PHOTO_UPLOAD (opcode 80) and the HTTP upload to MAX. How long
    MAX keeps an attachment is in API.md. Answers within ~27 s: the fetch at
    most 8 s, opcode 80 at most 4 s, the upload at most 15 s.

    Args:
        body (PhotoBody): One of `url` and `data`.
        body (UploadPhotoFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PhotoResponse]]
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
    body: Union[
        PhotoBody,
        UploadPhotoFilesBody,
    ],
) -> Optional[Union[ErrorResponse, PhotoResponse]]:
    """Upload a photo once

     Uploads a photo to MAX for the account and answers with its
    `attachment`, which `POST /chat/send/text` takes in `attachments` for
    any chat of the account. The photo comes as JSON `{url}` or `{data}`
    (base64 or a data URL), or as a multipart form with a `file` field. The
    body, and the photo, are at most `MAXAPI_PHOTO_MAX_BYTES` (10 MiB by
    default). A URL is fetched by the gateway through its SSRF guard (http
    and https only, no internal address, 8 s, a 2xx answer). The photo must
    be a JPEG, PNG, GIF or WebP image; `width` and `height` are read from
    it. Then PHOTO_UPLOAD (opcode 80) and the HTTP upload to MAX. How long
    MAX keeps an attachment is in API.md. Answers within ~27 s: the fetch at
    most 8 s, opcode 80 at most 4 s, the upload at most 15 s.

    Args:
        body (PhotoBody): One of `url` and `data`.
        body (UploadPhotoFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PhotoResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        PhotoBody,
        UploadPhotoFilesBody,
    ],
) -> Response[Union[ErrorResponse, PhotoResponse]]:
    """Upload a photo once

     Uploads a photo to MAX for the account and answers with its
    `attachment`, which `POST /chat/send/text` takes in `attachments` for
    any chat of the account. The photo comes as JSON `{url}` or `{data}`
    (base64 or a data URL), or as a multipart form with a `file` field. The
    body, and the photo, are at most `MAXAPI_PHOTO_MAX_BYTES` (10 MiB by
    default). A URL is fetched by the gateway through its SSRF guard (http
    and https only, no internal address, 8 s, a 2xx answer). The photo must
    be a JPEG, PNG, GIF or WebP image; `width` and `height` are read from
    it. Then PHOTO_UPLOAD (opcode 80) and the HTTP upload to MAX. How long
    MAX keeps an attachment is in API.md. Answers within ~27 s: the fetch at
    most 8 s, opcode 80 at most 4 s, the upload at most 15 s.

    Args:
        body (PhotoBody): One of `url` and `data`.
        body (UploadPhotoFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PhotoResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        PhotoBody,
        UploadPhotoFilesBody,
    ],
) -> Optional[Union[ErrorResponse, PhotoResponse]]:
    """Upload a photo once

     Uploads a photo to MAX for the account and answers with its
    `attachment`, which `POST /chat/send/text` takes in `attachments` for
    any chat of the account. The photo comes as JSON `{url}` or `{data}`
    (base64 or a data URL), or as a multipart form with a `file` field. The
    body, and the photo, are at most `MAXAPI_PHOTO_MAX_BYTES` (10 MiB by
    default). A URL is fetched by the gateway through its SSRF guard (http
    and https only, no internal address, 8 s, a 2xx answer). The photo must
    be a JPEG, PNG, GIF or WebP image; `width` and `height` are read from
    it. Then PHOTO_UPLOAD (opcode 80) and the HTTP upload to MAX. How long
    MAX keeps an attachment is in API.md. Answers within ~27 s: the fetch at
    most 8 s, opcode 80 at most 4 s, the upload at most 15 s.

    Args:
        body (PhotoBody): One of `url` and `data`.
        body (UploadPhotoFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PhotoResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
