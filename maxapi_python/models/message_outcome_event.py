from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageOutcomeEvent")


@_attrs_define
class MessageOutcomeEvent:
    """The outcome of a send with a `ref` answered `send_failed`: a minute (or
    3, or 10) after the send, the gateway found the message in the chat by
    its cid, or did not. No text is carried.

        Attributes:
            type_ (Literal['MessageOutcome']):
            ref (str): The caller's own id of the message, at most 128 bytes. The message's
                cid is made from it, the same for every send with this ref, and a
                `send_failed` with it is confirmed by `MessageOutcome`. Example: post-42-chat-7.
            chat_id (int):  Example: -70000000000000.
            delivered (bool):
            max_user_id (int): The MAX id of the account's MAX user Example: 123456789.
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
            event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
            message_id (Union[Unset, str]): MAX's id of the message, only when delivered Example: 115478893120847321.
    """

    type_: Literal["MessageOutcome"]
    ref: str
    chat_id: int
    delivered: bool
    max_user_id: int
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    message_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ref = self.ref

        chat_id = self.chat_id

        delivered = self.delivered

        max_user_id = self.max_user_id

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        message_id = self.message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ref": ref,
                "chatId": chat_id,
                "delivered": delivered,
                "maxUserID": max_user_id,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if message_id is not UNSET:
            field_dict["messageId"] = message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["MessageOutcome"], d.pop("type"))
        if type_ != "MessageOutcome":
            raise ValueError(f"type must match const 'MessageOutcome', got '{type_}'")

        ref = d.pop("ref")

        chat_id = d.pop("chatId")

        delivered = d.pop("delivered")

        max_user_id = d.pop("maxUserID")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        message_id = d.pop("messageId", UNSET)

        message_outcome_event = cls(
            type_=type_,
            ref=ref,
            chat_id=chat_id,
            delivered=delivered,
            max_user_id=max_user_id,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            message_id=message_id,
        )

        message_outcome_event.additional_properties = d
        return message_outcome_event

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
