from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.password_body import PasswordBody
from ...models.password_response import PasswordResponse
from ...types import Response


def _get_kwargs(
    *,
    body: PasswordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PasswordResponse]]:
    if response.status_code == 200:
        response_200 = PasswordResponse.from_dict(response.json())

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

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, PasswordResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PasswordBody,
) -> Response[Union[ErrorResponse, PasswordResponse]]:
    """Send the account's cloud password

     After the scan MAX asks for the cloud password of an account that has
    one (webhook `QRPasswordRequired`, `GET /session/qr` answers `409
    password_required`). This passes it to MAX (opcode 115). `200` means
    MAX took it: `QRAuthorized` and `Sync` follow. A wrong password
    answers `422 invalid_password` and may be sent again; the fifth
    refusal ends the login (`410 login_expired`). The password is never
    stored or logged.

    Args:
        body (PasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PasswordResponse]]
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
    body: PasswordBody,
) -> Optional[Union[ErrorResponse, PasswordResponse]]:
    """Send the account's cloud password

     After the scan MAX asks for the cloud password of an account that has
    one (webhook `QRPasswordRequired`, `GET /session/qr` answers `409
    password_required`). This passes it to MAX (opcode 115). `200` means
    MAX took it: `QRAuthorized` and `Sync` follow. A wrong password
    answers `422 invalid_password` and may be sent again; the fifth
    refusal ends the login (`410 login_expired`). The password is never
    stored or logged.

    Args:
        body (PasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PasswordResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PasswordBody,
) -> Response[Union[ErrorResponse, PasswordResponse]]:
    """Send the account's cloud password

     After the scan MAX asks for the cloud password of an account that has
    one (webhook `QRPasswordRequired`, `GET /session/qr` answers `409
    password_required`). This passes it to MAX (opcode 115). `200` means
    MAX took it: `QRAuthorized` and `Sync` follow. A wrong password
    answers `422 invalid_password` and may be sent again; the fifth
    refusal ends the login (`410 login_expired`). The password is never
    stored or logged.

    Args:
        body (PasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PasswordResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PasswordBody,
) -> Optional[Union[ErrorResponse, PasswordResponse]]:
    """Send the account's cloud password

     After the scan MAX asks for the cloud password of an account that has
    one (webhook `QRPasswordRequired`, `GET /session/qr` answers `409
    password_required`). This passes it to MAX (opcode 115). `200` means
    MAX took it: `QRAuthorized` and `Sync` follow. A wrong password
    answers `422 invalid_password` and may be sent again; the fifth
    refusal ends the login (`410 login_expired`). The password is never
    stored or logged.

    Args:
        body (PasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PasswordResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
