from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteMessagesBody")


@_attrs_define
class DeleteMessagesBody:
    """
    Attributes:
        chat_id (int):  Example: -70000000000000.
        message_ids (list[str]): The messages to delete for everyone, as `messageId` of a send (a JSON number is read
            too)
    """

    chat_id: int
    message_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        message_ids = self.message_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "messageIds": message_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        message_ids = cast(list[str], d.pop("messageIds"))

        delete_messages_body = cls(
            chat_id=chat_id,
            message_ids=message_ids,
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
