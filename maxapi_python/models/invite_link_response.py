from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteLinkResponse")


@_attrs_define
class InviteLinkResponse:
    """Response with group invite link

    Attributes:
        invite_link (Union[Unset, str]):  Example: https://max.ru/join/abc123.
        success (Union[Unset, bool]):  Example: True.
    """

    invite_link: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invite_link = self.invite_link

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invite_link is not UNSET:
            field_dict["inviteLink"] = invite_link
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invite_link = d.pop("inviteLink", UNSET)

        success = d.pop("success", UNSET)

        invite_link_response = cls(
            invite_link=invite_link,
            success=success,
        )

        invite_link_response.additional_properties = d
        return invite_link_response

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
