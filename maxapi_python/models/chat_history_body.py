from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatHistoryBody")


@_attrs_define
class ChatHistoryBody:
    """
    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        count (Union[Unset, int]):  Example: 50.
        from_time (Union[Unset, int]):
    """

    chat_id: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    from_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        count = self.count

        from_time = self.from_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if count is not UNSET:
            field_dict["count"] = count
        if from_time is not UNSET:
            field_dict["fromTime"] = from_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        count = d.pop("count", UNSET)

        from_time = d.pop("fromTime", UNSET)

        chat_history_body = cls(
            chat_id=chat_id,
            count=count,
            from_time=from_time,
        )

        chat_history_body.additional_properties = d
        return chat_history_body

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
