from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteMessagesBody")


@_attrs_define
class DeleteMessagesBody:
    """
    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        message_ids (Union[Unset, list[int]]):  Example: [115478893120847321].
        for_me (Union[Unset, bool]): Delete only for the account
    """

    chat_id: Union[Unset, int] = UNSET
    message_ids: Union[Unset, list[int]] = UNSET
    for_me: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        message_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.message_ids, Unset):
            message_ids = self.message_ids

        for_me = self.for_me

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if message_ids is not UNSET:
            field_dict["messageIds"] = message_ids
        if for_me is not UNSET:
            field_dict["forMe"] = for_me

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        message_ids = cast(list[int], d.pop("messageIds", UNSET))

        for_me = d.pop("forMe", UNSET)

        delete_messages_body = cls(
            chat_id=chat_id,
            message_ids=message_ids,
            for_me=for_me,
        )

        delete_messages_body.additional_properties = d
        return delete_messages_body

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
