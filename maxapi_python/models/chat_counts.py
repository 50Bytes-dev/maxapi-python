from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCounts")


@_attrs_define
class ChatCounts:
    """Counts of dialogs, groups and channels

    Attributes:
        channels (Union[Unset, int]):  Example: 3.
        dialogs (Union[Unset, int]):  Example: 15.
        groups (Union[Unset, int]):  Example: 8.
    """

    channels: Union[Unset, int] = UNSET
    dialogs: Union[Unset, int] = UNSET
    groups: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels = self.channels

        dialogs = self.dialogs

        groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if dialogs is not UNSET:
            field_dict["dialogs"] = dialogs
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channels = d.pop("channels", UNSET)

        dialogs = d.pop("dialogs", UNSET)

        groups = d.pop("groups", UNSET)

        chat_counts = cls(
            channels=channels,
            dialogs=dialogs,
            groups=groups,
        )

        chat_counts.additional_properties = d
        return chat_counts

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
