from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.max_reaction_counter import MaxReactionCounter


T = TypeVar("T", bound="MaxReactionInfo")


@_attrs_define
class MaxReactionInfo:
    """
    Attributes:
        total_count (Union[Unset, int]):
        your_reaction (Union[Unset, str]):
        counters (Union[Unset, list['MaxReactionCounter']]):
    """

    total_count: Union[Unset, int] = UNSET
    your_reaction: Union[Unset, str] = UNSET
    counters: Union[Unset, list["MaxReactionCounter"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        your_reaction = self.your_reaction

        counters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.counters, Unset):
            counters = []
            for counters_item_data in self.counters:
                counters_item = counters_item_data.to_dict()
                counters.append(counters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if your_reaction is not UNSET:
            field_dict["yourReaction"] = your_reaction
        if counters is not UNSET:
            field_dict["counters"] = counters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_reaction_counter import MaxReactionCounter

        d = dict(src_dict)
        total_count = d.pop("totalCount", UNSET)

        your_reaction = d.pop("yourReaction", UNSET)

        counters = []
        _counters = d.pop("counters", UNSET)
        for counters_item_data in _counters or []:
            counters_item = MaxReactionCounter.from_dict(counters_item_data)

            counters.append(counters_item)

        max_reaction_info = cls(
            total_count=total_count,
            your_reaction=your_reaction,
            counters=counters,
        )

        max_reaction_info.additional_properties = d
        return max_reaction_info

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
