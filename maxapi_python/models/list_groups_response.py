from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_groups_response_channels_item import ListGroupsResponseChannelsItem
    from ..models.list_groups_response_groups_item import ListGroupsResponseGroupsItem


T = TypeVar("T", bound="ListGroupsResponse")


@_attrs_define
class ListGroupsResponse:
    """Response with list of groups and channels

    Attributes:
        channels (Union[Unset, list['ListGroupsResponseChannelsItem']]):
        groups (Union[Unset, list['ListGroupsResponseGroupsItem']]):
        success (Union[Unset, bool]):  Example: True.
    """

    channels: Union[Unset, list["ListGroupsResponseChannelsItem"]] = UNSET
    groups: Union[Unset, list["ListGroupsResponseGroupsItem"]] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if groups is not UNSET:
            field_dict["groups"] = groups
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_groups_response_channels_item import ListGroupsResponseChannelsItem
        from ..models.list_groups_response_groups_item import ListGroupsResponseGroupsItem

        d = dict(src_dict)
        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = ListGroupsResponseChannelsItem.from_dict(channels_item_data)

            channels.append(channels_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ListGroupsResponseGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        success = d.pop("success", UNSET)

        list_groups_response = cls(
            channels=channels,
            groups=groups,
            success=success,
        )

        list_groups_response.additional_properties = d
        return list_groups_response

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
