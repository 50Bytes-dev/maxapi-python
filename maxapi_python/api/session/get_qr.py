from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.qr_response import QRResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/session/qr",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, QRResponse]]:
    if response.status_code == 200:
        response_200 = QRResponse.from_dict(response.json())

        return response_200

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
) -> Response[Union[ErrorResponse, QRResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, QRResponse]]:
    """Get the QR of the running login

     The QR of the running QR login as a PNG data URL. The gateway issues a
    new QR when MAX's expires (webhook `QRGenerated`), so poll it every few
    seconds while it is shown. There is no `scanned` flag: the scan arrives
    as `QRScanned`, the login as `QRAuthorized` and `Sync`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QRResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, QRResponse]]:
    """Get the QR of the running login

     The QR of the running QR login as a PNG data URL. The gateway issues a
    new QR when MAX's expires (webhook `QRGenerated`), so poll it every few
    seconds while it is shown. There is no `scanned` flag: the scan arrives
    as `QRScanned`, the login as `QRAuthorized` and `Sync`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, QRResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, QRResponse]]:
    """Get the QR of the running login

     The QR of the running QR login as a PNG data URL. The gateway issues a
    new QR when MAX's expires (webhook `QRGenerated`), so poll it every few
    seconds while it is shown. There is no `scanned` flag: the scan arrives
    as `QRScanned`, the login as `QRAuthorized` and `Sync`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QRResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, QRResponse]]:
    """Get the QR of the running login

     The QR of the running QR login as a PNG data URL. The gateway issues a
    new QR when MAX's expires (webhook `QRGenerated`), so poll it every few
    seconds while it is shown. There is no `scanned` flag: the scan arrives
    as `QRScanned`, the login as `QRAuthorized` and `Sync`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, QRResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
