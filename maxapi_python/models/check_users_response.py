from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.check_users_result import CheckUsersResult


T = TypeVar("T", bound="CheckUsersResponse")


@_attrs_define
class CheckUsersResponse:
    """
    Attributes:
        success (bool):  Example: True.
        users (list['CheckUsersResult']):
    """

    success: bool
    users: list["CheckUsersResult"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_users_result import CheckUsersResult

        d = dict(src_dict)
        success = d.pop("success")

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = CheckUsersResult.from_dict(users_item_data)

            users.append(users_item)

        check_users_response = cls(
            success=success,
            users=users,
        )

        check_users_response.additional_properties = d
        return check_users_response

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
