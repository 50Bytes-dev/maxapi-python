from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_history_response_messages_item import ChatHistoryResponseMessagesItem


T = TypeVar("T", bound="ChatHistoryResponse")


@_attrs_define
class ChatHistoryResponse:
    """Response with chat history messages

    Attributes:
        messages (Union[Unset, list['ChatHistoryResponseMessagesItem']]):
        success (Union[Unset, bool]):  Example: True.
    """

    messages: Union[Unset, list["ChatHistoryResponseMessagesItem"]] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_history_response_messages_item import ChatHistoryResponseMessagesItem

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ChatHistoryResponseMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        success = d.pop("success", UNSET)

        chat_history_response = cls(
            messages=messages,
            success=success,
        )

        chat_history_response.additional_properties = d
        return chat_history_response

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
