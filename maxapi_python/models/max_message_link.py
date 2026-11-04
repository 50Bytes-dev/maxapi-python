from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.max_message import MaxMessage


T = TypeVar("T", bound="MaxMessageLink")


@_attrs_define
class MaxMessageLink:
    """A reply or forward link of a message

    Attributes:
        type_ (Union[Unset, str]):  Example: REPLY.
        chat_id (Union[Unset, int]):
        message_id (Union[Unset, str]):
        message (Union[Unset, MaxMessage]): A message, as MAX gives it
    """

    type_: Union[Unset, str] = UNSET
    chat_id: Union[Unset, int] = UNSET
    message_id: Union[Unset, str] = UNSET
    message: Union[Unset, "MaxMessage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        chat_id = self.chat_id

        message_id = self.message_id

        message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_message import MaxMessage

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        chat_id = d.pop("chatId", UNSET)

        message_id = d.pop("messageId", UNSET)

        _message = d.pop("message", UNSET)
        message: Union[Unset, MaxMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = MaxMessage.from_dict(_message)

        max_message_link = cls(
            type_=type_,
            chat_id=chat_id,
            message_id=message_id,
            message=message,
        )

        max_message_link.additional_properties = d
        return max_message_link

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
