from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendTextBody")


@_attrs_define
class SendTextBody:
    """One of `chatId` and `phone` is required; with both, `chatId` wins. A message needs a text or an attachment. Unknown
    fields are ignored.

        Attributes:
            chat_id (Union[Unset, int]): The chat, as `chatId` of `GET /chat/list`: a dialog (positive), a
                group chat or channel (negative). 0 means none (chat 0 is the
                account's own Favorites and is never addressed here). Example: -70000000000000.
            phone (Union[Unset, str]): The recipient's phone with country code; looked up in the cache, then in MAX. The
                cache key is the string exactly as sent. Example: 79001234567.
            text (Union[Unset, str]): At most 4000 UTF-16 code units (an emoji is 2); may be empty when `attachments` has
                one. Example: Заказ 123 готов к выдаче.
            attachments (Union[Unset, list[str]]): Photos, as `attachment` of `POST /media/photo`, in this order; 12 is
                MAX's own limit Example: ['AAAA...photo-token'].
            ref (Union[Unset, str]): The caller's own id of the message, at most 128 bytes. The message's
                cid is made from it, the same for every send with this ref, and a
                `send_failed` with it is confirmed by `MessageOutcome`. Example: post-42-chat-7.
            reply_to (Union[Unset, str]): A MAX message id. MAX's ids are above 2^53, so they travel as strings; a JSON
                number is read too. Example: 115478893120847321.
            notify (Union[Unset, bool]): Whether MAX notifies the recipients; true when left out, as MAX's web client sends
                every message. MAX refuses a channel post with false. Default: True. Example: True.
    """

    chat_id: Union[Unset, int] = UNSET
    phone: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    attachments: Union[Unset, list[str]] = UNSET
    ref: Union[Unset, str] = UNSET
    reply_to: Union[Unset, str] = UNSET
    notify: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        phone = self.phone

        text = self.text

        attachments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        ref = self.ref

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
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if ref is not UNSET:
            field_dict["ref"] = ref
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

        attachments = cast(list[str], d.pop("attachments", UNSET))

        ref = d.pop("ref", UNSET)

        reply_to = d.pop("replyTo", UNSET)

        notify = d.pop("notify", UNSET)

        send_text_body = cls(
            chat_id=chat_id,
            phone=phone,
            text=text,
            attachments=attachments,
            ref=ref,
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
