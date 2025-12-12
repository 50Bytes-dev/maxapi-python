from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_user_result_item import CheckUserResultItem


T = TypeVar("T", bound="CheckUserResponse")


@_attrs_define
class CheckUserResponse:
    """Response with user existence check results

    Attributes:
        success (Union[Unset, bool]):  Example: True.
        users (Union[Unset, list['CheckUserResultItem']]):
    """

    success: Union[Unset, bool] = UNSET
    users: Union[Unset, list["CheckUserResultItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_user_result_item import CheckUserResultItem

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = CheckUserResultItem.from_dict(users_item_data)

            users.append(users_item)

        check_user_response = cls(
            success=success,
            users=users,
        )

        check_user_response.additional_properties = d
        return check_user_response

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
