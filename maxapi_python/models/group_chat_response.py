from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_chat_response_chat import GroupChatResponseChat


T = TypeVar("T", bound="GroupChatResponse")


@_attrs_define
class GroupChatResponse:
    """Response with group or chat information

    Attributes:
        chat (Union[Unset, GroupChatResponseChat]):
        success (Union[Unset, bool]):  Example: True.
    """

    chat: Union[Unset, "GroupChatResponseChat"] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.chat, Unset):
            chat = self.chat.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat is not UNSET:
            field_dict["chat"] = chat
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_chat_response_chat import GroupChatResponseChat

        d = dict(src_dict)
        _chat = d.pop("chat", UNSET)
        chat: Union[Unset, GroupChatResponseChat]
        if isinstance(_chat, Unset):
            chat = UNSET
        else:
            chat = GroupChatResponseChat.from_dict(_chat)

        success = d.pop("success", UNSET)

        group_chat_response = cls(
            chat=chat,
            success=success,
        )

        group_chat_response.additional_properties = d
        return group_chat_response

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
