from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusResponse")


@_attrs_define
class StatusResponse:
    """
    Attributes:
        success (bool):  Example: True.
        connected (bool): The account's MAX session is up. A running QR login is not a session (false). A paused account
            keeps its session.
        authenticated (bool): A MAX login (auth token) is stored
        logged_in (bool): `connected` and `authenticated`
        max_user_id (int): The MAX id of the session's account; 0 while no logged-in session is up Example: 123456789.
        paused (bool): Whether sending from the MAX account is paused: the live session's
            account, or without a session the one stored at the last login. Read
            it before `connected`.
        pause_reason (Union[Unset, str]): Why the MAX account is paused. maxapi gives only `spam` (a limit or
            restriction error of MAX). Example: spam.
        upstream_code (Union[Unset, str]): Only while paused; the MAX error code that paused the account Example:
            error.user.restricted.send.
        name (Union[Unset, str]): The MAX account's name, from the live session or else the last login; absent when
            unknown Example: Магазин у дома.
        photo (Union[Unset, str]): The MAX account's photo URL, as `name` Example: https://i.oneme.ru/i?r=....
    """

    success: bool
    connected: bool
    authenticated: bool
    logged_in: bool
    max_user_id: int
    paused: bool
    pause_reason: Union[Unset, str] = UNSET
    upstream_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    photo: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        connected = self.connected

        authenticated = self.authenticated

        logged_in = self.logged_in

        max_user_id = self.max_user_id

        paused = self.paused

        pause_reason = self.pause_reason

        upstream_code = self.upstream_code

        name = self.name

        photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "connected": connected,
                "authenticated": authenticated,
                "loggedIn": logged_in,
                "maxUserID": max_user_id,
                "paused": paused,
            }
        )
        if pause_reason is not UNSET:
            field_dict["pauseReason"] = pause_reason
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if name is not UNSET:
            field_dict["name"] = name
        if photo is not UNSET:
            field_dict["photo"] = photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        connected = d.pop("connected")

        authenticated = d.pop("authenticated")

        logged_in = d.pop("loggedIn")

        max_user_id = d.pop("maxUserID")

        paused = d.pop("paused")

        pause_reason = d.pop("pauseReason", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        name = d.pop("name", UNSET)

        photo = d.pop("photo", UNSET)

        status_response = cls(
            success=success,
            connected=connected,
            authenticated=authenticated,
            logged_in=logged_in,
            max_user_id=max_user_id,
            paused=paused,
            pause_reason=pause_reason,
            upstream_code=upstream_code,
            name=name,
            photo=photo,
        )

        status_response.additional_properties = d
        return status_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
