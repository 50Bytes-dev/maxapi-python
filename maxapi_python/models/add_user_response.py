from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddUserResponse")


@_attrs_define
class AddUserResponse:
    """Response after creating a new user

    Attributes:
        id (Union[Unset, str]):  Example: a7e5dd6b-8b3e-4035-ba87-3f96a0e3f5c0.
        name (Union[Unset, str]):  Example: John Doe.
        success (Union[Unset, bool]):  Example: True.
        token (Union[Unset, str]):  Example: abc123def456.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        success = self.success

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if success is not UNSET:
            field_dict["success"] = success
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        success = d.pop("success", UNSET)

        token = d.pop("token", UNSET)

        add_user_response = cls(
            id=id,
            name=name,
            success=success,
            token=token,
        )

        add_user_response.additional_properties = d
        return add_user_response

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
