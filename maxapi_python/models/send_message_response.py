from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageResponse")


@_attrs_define
class SendMessageResponse:
    """Response after sending a message

    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        message_id (Union[Unset, int]):  Example: 987654321.
        success (Union[Unset, bool]):  Example: True.
    """

    chat_id: Union[Unset, int] = UNSET
    message_id: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        message_id = self.message_id

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        message_id = d.pop("messageId", UNSET)

        success = d.pop("success", UNSET)

        send_message_response = cls(
            chat_id=chat_id,
            message_id=message_id,
            success=success,
        )

        send_message_response.additional_properties = d
        return send_message_response

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
