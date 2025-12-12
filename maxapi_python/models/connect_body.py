from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectBody")


@_attrs_define
class ConnectBody:
    """
    Attributes:
        immediate (Union[Unset, bool]):
        subscribe (Union[Unset, list[str]]):  Example: ['Message', 'ReadReceipt'].
    """

    immediate: Union[Unset, bool] = UNSET
    subscribe: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        immediate = self.immediate

        subscribe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscribe, Unset):
            subscribe = self.subscribe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if immediate is not UNSET:
            field_dict["immediate"] = immediate
        if subscribe is not UNSET:
            field_dict["subscribe"] = subscribe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        immediate = d.pop("immediate", UNSET)

        subscribe = cast(list[str], d.pop("subscribe", UNSET))

        connect_body = cls(
            immediate=immediate,
            subscribe=subscribe,
        )

        connect_body.additional_properties = d
        return connect_body

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
