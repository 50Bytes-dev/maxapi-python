from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """
    Attributes:
        authenticated (Union[Unset, bool]):  Example: True.
        connected (Union[Unset, int]):  Example: 1.
        events (Union[Unset, str]):  Example: All.
        id (Union[Unset, str]):  Example: a7e5dd6b-8b3e-4035-ba87-3f96a0e3f5c0.
        max_user_id (Union[Unset, int]):  Example: 123456789.
        name (Union[Unset, str]):  Example: John Doe.
        token (Union[Unset, str]):  Example: abc123def456.
        webhook (Union[Unset, str]):  Example: https://example.com/webhook.
    """

    authenticated: Union[Unset, bool] = UNSET
    connected: Union[Unset, int] = UNSET
    events: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    max_user_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    webhook: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authenticated = self.authenticated

        connected = self.connected

        events = self.events

        id = self.id

        max_user_id = self.max_user_id

        name = self.name

        token = self.token

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if connected is not UNSET:
            field_dict["connected"] = connected
        if events is not UNSET:
            field_dict["events"] = events
        if id is not UNSET:
            field_dict["id"] = id
        if max_user_id is not UNSET:
            field_dict["maxUserId"] = max_user_id
        if name is not UNSET:
            field_dict["name"] = name
        if token is not UNSET:
            field_dict["token"] = token
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authenticated = d.pop("authenticated", UNSET)

        connected = d.pop("connected", UNSET)

        events = d.pop("events", UNSET)

        id = d.pop("id", UNSET)

        max_user_id = d.pop("maxUserId", UNSET)

        name = d.pop("name", UNSET)

        token = d.pop("token", UNSET)

        webhook = d.pop("webhook", UNSET)

        user_response = cls(
            authenticated=authenticated,
            connected=connected,
            events=events,
            id=id,
            max_user_id=max_user_id,
            name=name,
            token=token,
            webhook=webhook,
        )

        user_response.additional_properties = d
        return user_response

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
