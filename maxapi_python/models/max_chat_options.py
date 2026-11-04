from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaxChatOptions")


@_attrs_define
class MaxChatOptions:
    """
    Attributes:
        only_owner_can_change_icon_title (Union[Unset, bool]):
        all_can_pin_message (Union[Unset, bool]):
        only_admin_can_add_member (Union[Unset, bool]):
        only_admin_can_call (Union[Unset, bool]):
        members_can_see_private_link (Union[Unset, bool]):
    """

    only_owner_can_change_icon_title: Union[Unset, bool] = UNSET
    all_can_pin_message: Union[Unset, bool] = UNSET
    only_admin_can_add_member: Union[Unset, bool] = UNSET
    only_admin_can_call: Union[Unset, bool] = UNSET
    members_can_see_private_link: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        only_owner_can_change_icon_title = self.only_owner_can_change_icon_title

        all_can_pin_message = self.all_can_pin_message

        only_admin_can_add_member = self.only_admin_can_add_member

        only_admin_can_call = self.only_admin_can_call

        members_can_see_private_link = self.members_can_see_private_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if only_owner_can_change_icon_title is not UNSET:
            field_dict["ONLY_OWNER_CAN_CHANGE_ICON_TITLE"] = only_owner_can_change_icon_title
        if all_can_pin_message is not UNSET:
            field_dict["ALL_CAN_PIN_MESSAGE"] = all_can_pin_message
        if only_admin_can_add_member is not UNSET:
            field_dict["ONLY_ADMIN_CAN_ADD_MEMBER"] = only_admin_can_add_member
        if only_admin_can_call is not UNSET:
            field_dict["ONLY_ADMIN_CAN_CALL"] = only_admin_can_call
        if members_can_see_private_link is not UNSET:
            field_dict["MEMBERS_CAN_SEE_PRIVATE_LINK"] = members_can_see_private_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        only_owner_can_change_icon_title = d.pop("ONLY_OWNER_CAN_CHANGE_ICON_TITLE", UNSET)

        all_can_pin_message = d.pop("ALL_CAN_PIN_MESSAGE", UNSET)

        only_admin_can_add_member = d.pop("ONLY_ADMIN_CAN_ADD_MEMBER", UNSET)

        only_admin_can_call = d.pop("ONLY_ADMIN_CAN_CALL", UNSET)

        members_can_see_private_link = d.pop("MEMBERS_CAN_SEE_PRIVATE_LINK", UNSET)

        max_chat_options = cls(
            only_owner_can_change_icon_title=only_owner_can_change_icon_title,
            all_can_pin_message=all_can_pin_message,
            only_admin_can_add_member=only_admin_can_add_member,
            only_admin_can_call=only_admin_can_call,
            members_can_see_private_link=members_can_see_private_link,
        )

        max_chat_options.additional_properties = d
        return max_chat_options

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
