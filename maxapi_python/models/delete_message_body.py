from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteMessageBody")


@_attrs_define
class DeleteMessageBody:
    """
    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        for_me (Union[Unset, bool]):
        message_ids (Union[Unset, list[int]]):
    """

    chat_id: Union[Unset, int] = UNSET
    for_me: Union[Unset, bool] = UNSET
    message_ids: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        for_me = self.for_me

        message_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.message_ids, Unset):
            message_ids = self.message_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if for_me is not UNSET:
            field_dict["forMe"] = for_me
        if message_ids is not UNSET:
            field_dict["messageIds"] = message_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        for_me = d.pop("forMe", UNSET)

        message_ids = cast(list[int], d.pop("messageIds", UNSET))

        delete_message_body = cls(
            chat_id=chat_id,
            for_me=for_me,
            message_ids=message_ids,
        )

        delete_message_body.additional_properties = d
        return delete_message_body

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
