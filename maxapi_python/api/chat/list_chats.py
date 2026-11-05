from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_include import ChatInclude
from ...models.chat_kind import ChatKind
from ...models.chat_list_response import ChatListResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    marker: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[ChatKind]] = UNSET,
    q: Union[Unset, str] = UNSET,
    include: Union[Unset, list[ChatInclude]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["marker"] = marker

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params["q"] = q

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = []
        for include_item_data in include:
            include_item = include_item_data.value
            json_include.append(include_item)

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chat/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChatListResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = ChatListResponse.from_dict(response.json())

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
) -> Response[Union[ChatListResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    marker: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[ChatKind]] = UNSET,
    q: Union[Unset, str] = UNSET,
    include: Union[Unset, list[ChatInclude]] = UNSET,
) -> Response[Union[ChatListResponse, ErrorResponse]]:
    """List the account's chats

     A page of the account's chats, the newest first, as the MAX web client
    pages them (CHATS_LIST, opcode 53). Each row carries the `chatId` a
    send takes and whether the account may write there. No message's text
    is in the answer unless `include=lastMessage` asks for it. The
    account's own Favorites (chat 0) is not listed.

    Pages follow MAX's cursor: pass `nextMarker` as `marker` to get the next
    page; without `nextMarker` this is the last one. MAX sets the page size
    (50 at the time of writing). `type` keeps the rows of the given kinds of
    each page, and `q` the rows whose title (a dialog's: the person's name)
    holds it, in any letter case, so a page may hold fewer rows, even none,
    while `nextMarker` is still there: page on while it is present. MAX's
    own search (opcode 68) is not used: live it found none of the
    account's chats by title. One MAX call for the page, one for the people
    behind its dialogs (their names and photos): answers within ~7 s.

    Args:
        marker (Union[Unset, str]):
        type_ (Union[Unset, list[ChatKind]]):
        q (Union[Unset, str]):
        include (Union[Unset, list[ChatInclude]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatListResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        marker=marker,
        type_=type_,
        q=q,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    marker: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[ChatKind]] = UNSET,
    q: Union[Unset, str] = UNSET,
    include: Union[Unset, list[ChatInclude]] = UNSET,
) -> Optional[Union[ChatListResponse, ErrorResponse]]:
    """List the account's chats

     A page of the account's chats, the newest first, as the MAX web client
    pages them (CHATS_LIST, opcode 53). Each row carries the `chatId` a
    send takes and whether the account may write there. No message's text
    is in the answer unless `include=lastMessage` asks for it. The
    account's own Favorites (chat 0) is not listed.

    Pages follow MAX's cursor: pass `nextMarker` as `marker` to get the next
    page; without `nextMarker` this is the last one. MAX sets the page size
    (50 at the time of writing). `type` keeps the rows of the given kinds of
    each page, and `q` the rows whose title (a dialog's: the person's name)
    holds it, in any letter case, so a page may hold fewer rows, even none,
    while `nextMarker` is still there: page on while it is present. MAX's
    own search (opcode 68) is not used: live it found none of the
    account's chats by title. One MAX call for the page, one for the people
    behind its dialogs (their names and photos): answers within ~7 s.

    Args:
        marker (Union[Unset, str]):
        type_ (Union[Unset, list[ChatKind]]):
        q (Union[Unset, str]):
        include (Union[Unset, list[ChatInclude]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatListResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        marker=marker,
        type_=type_,
        q=q,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    marker: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[ChatKind]] = UNSET,
    q: Union[Unset, str] = UNSET,
    include: Union[Unset, list[ChatInclude]] = UNSET,
) -> Response[Union[ChatListResponse, ErrorResponse]]:
    """List the account's chats

     A page of the account's chats, the newest first, as the MAX web client
    pages them (CHATS_LIST, opcode 53). Each row carries the `chatId` a
    send takes and whether the account may write there. No message's text
    is in the answer unless `include=lastMessage` asks for it. The
    account's own Favorites (chat 0) is not listed.

    Pages follow MAX's cursor: pass `nextMarker` as `marker` to get the next
    page; without `nextMarker` this is the last one. MAX sets the page size
    (50 at the time of writing). `type` keeps the rows of the given kinds of
    each page, and `q` the rows whose title (a dialog's: the person's name)
    holds it, in any letter case, so a page may hold fewer rows, even none,
    while `nextMarker` is still there: page on while it is present. MAX's
    own search (opcode 68) is not used: live it found none of the
    account's chats by title. One MAX call for the page, one for the people
    behind its dialogs (their names and photos): answers within ~7 s.

    Args:
        marker (Union[Unset, str]):
        type_ (Union[Unset, list[ChatKind]]):
        q (Union[Unset, str]):
        include (Union[Unset, list[ChatInclude]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatListResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        marker=marker,
        type_=type_,
        q=q,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    marker: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[ChatKind]] = UNSET,
    q: Union[Unset, str] = UNSET,
    include: Union[Unset, list[ChatInclude]] = UNSET,
) -> Optional[Union[ChatListResponse, ErrorResponse]]:
    """List the account's chats

     A page of the account's chats, the newest first, as the MAX web client
    pages them (CHATS_LIST, opcode 53). Each row carries the `chatId` a
    send takes and whether the account may write there. No message's text
    is in the answer unless `include=lastMessage` asks for it. The
    account's own Favorites (chat 0) is not listed.

    Pages follow MAX's cursor: pass `nextMarker` as `marker` to get the next
    page; without `nextMarker` this is the last one. MAX sets the page size
    (50 at the time of writing). `type` keeps the rows of the given kinds of
    each page, and `q` the rows whose title (a dialog's: the person's name)
    holds it, in any letter case, so a page may hold fewer rows, even none,
    while `nextMarker` is still there: page on while it is present. MAX's
    own search (opcode 68) is not used: live it found none of the
    account's chats by title. One MAX call for the page, one for the people
    behind its dialogs (their names and photos): answers within ~7 s.

    Args:
        marker (Union[Unset, str]):
        type_ (Union[Unset, list[ChatKind]]):
        q (Union[Unset, str]):
        include (Union[Unset, list[ChatInclude]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatListResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            marker=marker,
            type_=type_,
            q=q,
            include=include,
        )
    ).parsed
