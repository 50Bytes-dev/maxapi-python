from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckUsersResult")


@_attrs_define
class CheckUsersResult:
    """
    Attributes:
        phone (str):  Example: 79001234567.
        exists (bool): MAX has a user with the number Example: True.
        max_user_id (int): The user's MAX id; 0 when not found Example: 987654321.
        name (Union[Unset, str]): The user's first name in MAX, when found Example: Иван.
        error (Union[Unset, str]): Present when the lookup itself failed; `exists` false then does not mean that MAX has
            no such user Example: Timeout Error: Request timed out.
    """

    phone: str
    exists: bool
    max_user_id: int
    name: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        exists = self.exists

        max_user_id = self.max_user_id

        name = self.name

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone": phone,
                "exists": exists,
                "maxUserId": max_user_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone = d.pop("phone")

        exists = d.pop("exists")

        max_user_id = d.pop("maxUserId")

        name = d.pop("name", UNSET)

        error = d.pop("error", UNSET)

        check_users_result = cls(
            phone=phone,
            exists=exists,
            max_user_id=max_user_id,
            name=name,
            error=error,
        )

        check_users_result.additional_properties = d
        return check_users_result

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
