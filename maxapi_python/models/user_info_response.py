from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_info_response_users_item import UserInfoResponseUsersItem


T = TypeVar("T", bound="UserInfoResponse")


@_attrs_define
class UserInfoResponse:
    """Response with user information (always returns array)

    Attributes:
        count (Union[Unset, int]):  Example: 1.
        success (Union[Unset, bool]):  Example: True.
        users (Union[Unset, list['UserInfoResponseUsersItem']]):
    """

    count: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    users: Union[Unset, list["UserInfoResponseUsersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

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
        if count is not UNSET:
            field_dict["count"] = count
        if success is not UNSET:
            field_dict["success"] = success
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_info_response_users_item import UserInfoResponseUsersItem

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        success = d.pop("success", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserInfoResponseUsersItem.from_dict(users_item_data)

            users.append(users_item)

        user_info_response = cls(
            count=count,
            success=success,
            users=users,
        )

        user_info_response.additional_properties = d
        return user_info_response

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
