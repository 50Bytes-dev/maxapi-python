from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendTextBody")


@_attrs_define
class SendTextBody:
    """One of `chatId` and `phone` is required; with both, `chatId` wins. Unknown fields are ignored.

    Attributes:
        chat_id (Union[Unset, int]): The MAX chat id. 0 means none (chat 0 is the account's own Favorites and is never
            addressed here). Example: 123456789.
        phone (Union[Unset, str]): The recipient's phone with country code; looked up in the cache, then in MAX. The
            cache key is the string exactly as sent. Example: 79001234567.
        text (Union[Unset, str]):  Example: Заказ 123 готов к выдаче.
        reply_to (Union[Unset, int]): Id of the message to reply to; 0 for none
        notify (Union[Unset, bool]): Whether MAX notifies the recipient; default false Example: True.
    """

    chat_id: Union[Unset, int] = UNSET
    phone: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    reply_to: Union[Unset, int] = UNSET
    notify: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        phone = self.phone

        text = self.text

        reply_to = self.reply_to

        notify = self.notify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if text is not UNSET:
            field_dict["text"] = text
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if notify is not UNSET:
            field_dict["notify"] = notify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        phone = d.pop("phone", UNSET)

        text = d.pop("text", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        notify = d.pop("notify", UNSET)

        send_text_body = cls(
            chat_id=chat_id,
            phone=phone,
            text=text,
            reply_to=reply_to,
            notify=notify,
        )

        send_text_body.additional_properties = d
        return send_text_body

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
