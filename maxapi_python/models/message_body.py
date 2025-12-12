from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageBody")


@_attrs_define
class MessageBody:
    """
    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        notify (Union[Unset, bool]):  Example: True.
        phone (Union[Unset, str]):  Example: 79001234567.
        reply_to (Union[Unset, int]):
        text (Union[Unset, str]):  Example: Hello, World!.
    """

    chat_id: Union[Unset, int] = UNSET
    notify: Union[Unset, bool] = UNSET
    phone: Union[Unset, str] = UNSET
    reply_to: Union[Unset, int] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        notify = self.notify

        phone = self.phone

        reply_to = self.reply_to

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if notify is not UNSET:
            field_dict["notify"] = notify
        if phone is not UNSET:
            field_dict["phone"] = phone
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        notify = d.pop("notify", UNSET)

        phone = d.pop("phone", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        text = d.pop("text", UNSET)

        message_body = cls(
            chat_id=chat_id,
            notify=notify,
            phone=phone,
            reply_to=reply_to,
            text=text,
        )

        message_body.additional_properties = d
        return message_body

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
