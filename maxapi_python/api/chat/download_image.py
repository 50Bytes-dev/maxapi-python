from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_media_response import DownloadMediaResponse
from ...models.download_url_body import DownloadUrlBody
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DownloadUrlBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/downloadimage",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DownloadMediaResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DownloadMediaResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DownloadMediaResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DownloadUrlBody,
) -> Response[Union[DownloadMediaResponse, ErrorResponse]]:
    """Download a file by URL

     The gateway fetches `url` itself through its SSRF guard (http and https
    only, no internal address, at most `MAXAPI_MEDIA_MAX_BYTES`, 60 s) and
    returns the bytes in base64. Meant for the `baseUrl` of a photo of a
    `Message`. Makes no MAX call and needs no MAX session.

    Args:
        body (DownloadUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DownloadMediaResponse, ErrorResponse]]
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
    body: DownloadUrlBody,
) -> Optional[Union[DownloadMediaResponse, ErrorResponse]]:
    """Download a file by URL

     The gateway fetches `url` itself through its SSRF guard (http and https
    only, no internal address, at most `MAXAPI_MEDIA_MAX_BYTES`, 60 s) and
    returns the bytes in base64. Meant for the `baseUrl` of a photo of a
    `Message`. Makes no MAX call and needs no MAX session.

    Args:
        body (DownloadUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DownloadMediaResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DownloadUrlBody,
) -> Response[Union[DownloadMediaResponse, ErrorResponse]]:
    """Download a file by URL

     The gateway fetches `url` itself through its SSRF guard (http and https
    only, no internal address, at most `MAXAPI_MEDIA_MAX_BYTES`, 60 s) and
    returns the bytes in base64. Meant for the `baseUrl` of a photo of a
    `Message`. Makes no MAX call and needs no MAX session.

    Args:
        body (DownloadUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DownloadMediaResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DownloadUrlBody,
) -> Optional[Union[DownloadMediaResponse, ErrorResponse]]:
    """Download a file by URL

     The gateway fetches `url` itself through its SSRF guard (http and https
    only, no internal address, at most `MAXAPI_MEDIA_MAX_BYTES`, 60 s) and
    returns the bytes in base64. Meant for the `baseUrl` of a photo of a
    `Message`. Makes no MAX call and needs no MAX session.

    Args:
        body (DownloadUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DownloadMediaResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
