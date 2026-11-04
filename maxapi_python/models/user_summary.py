from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserSummary")


@_attrs_define
class UserSummary:
    """
    Attributes:
        id (str):  Example: 6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        name (str):  Example: Shop bot.
        token (str): The account token Example: 0b7a9e31-5d2c-4f6a-9e8b-1c2d3e4f5a6b.
        max_user_id (Union[None, int]): The MAX id stored at the last login; null before the first Example: 123456789.
        webhook (str):  Example: https://example.com/webhook.
        events (str): The stored subscription, comma-separated Example: Sync,QRAuthorized,AuthExpired,LoggedOut.
        connected (int): The stored connected flag, 1 or 0 (not the live session) Example: 1.
        authenticated (bool): A MAX login is stored Example: True.
    """

    id: str
    name: str
    token: str
    max_user_id: Union[None, int]
    webhook: str
    events: str
    connected: int
    authenticated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        token = self.token

        max_user_id: Union[None, int]
        max_user_id = self.max_user_id

        webhook = self.webhook

        events = self.events

        connected = self.connected

        authenticated = self.authenticated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "token": token,
                "maxUserId": max_user_id,
                "webhook": webhook,
                "events": events,
                "connected": connected,
                "authenticated": authenticated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        token = d.pop("token")

        def _parse_max_user_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        max_user_id = _parse_max_user_id(d.pop("maxUserId"))

        webhook = d.pop("webhook")

        events = d.pop("events")

        connected = d.pop("connected")

        authenticated = d.pop("authenticated")

        user_summary = cls(
            id=id,
            name=name,
            token=token,
            max_user_id=max_user_id,
            webhook=webhook,
            events=events,
            connected=connected,
            authenticated=authenticated,
        )

        user_summary.additional_properties = d
        return user_summary

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
