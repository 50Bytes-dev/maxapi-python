from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddUserBody")


@_attrs_define
class AddUserBody:
    """
    Attributes:
        events (Union[Unset, str]):  Example: All.
        name (Union[Unset, str]):  Example: John Doe.
        webhook (Union[Unset, str]):  Example: https://example.com/webhook.
    """

    events: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    webhook: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = self.events

        name = self.name

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if name is not UNSET:
            field_dict["name"] = name
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = d.pop("events", UNSET)

        name = d.pop("name", UNSET)

        webhook = d.pop("webhook", UNSET)

        add_user_body = cls(
            events=events,
            name=name,
            webhook=webhook,
        )

        add_user_body.additional_properties = d
        return add_user_body

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
