from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_row import ChatRow


T = TypeVar("T", bound="ChatListResponse")


@_attrs_define
class ChatListResponse:
    """
    Attributes:
        success (bool):  Example: True.
        items (list['ChatRow']):
        next_marker (Union[Unset, str]): Present when another page follows; pass it as `marker` Example: 1776820000000.
    """

    success: bool
    items: list["ChatRow"]
    next_marker: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_marker = self.next_marker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "items": items,
            }
        )
        if next_marker is not UNSET:
            field_dict["nextMarker"] = next_marker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_row import ChatRow

        d = dict(src_dict)
        success = d.pop("success")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ChatRow.from_dict(items_item_data)

            items.append(items_item)

        next_marker = d.pop("nextMarker", UNSET)

        chat_list_response = cls(
            success=success,
            items=items,
            next_marker=next_marker,
        )

        chat_list_response.additional_properties = d
        return chat_list_response

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
