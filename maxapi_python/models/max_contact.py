from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.max_name import MaxName


T = TypeVar("T", bound="MaxContact")


@_attrs_define
class MaxContact:
    """A contact, as MAX gives it

    Attributes:
        id (int):  Example: 987654321.
        account_status (Union[Unset, int]):
        base_raw_url (Union[Unset, str]):
        base_url (Union[Unset, str]):
        names (Union[Unset, list['MaxName']]):
        options (Union[Unset, list[str]]):
        photo_id (Union[Unset, int]):
        update_time (Union[Unset, int]):
    """

    id: int
    account_status: Union[Unset, int] = UNSET
    base_raw_url: Union[Unset, str] = UNSET
    base_url: Union[Unset, str] = UNSET
    names: Union[Unset, list["MaxName"]] = UNSET
    options: Union[Unset, list[str]] = UNSET
    photo_id: Union[Unset, int] = UNSET
    update_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_status = self.account_status

        base_raw_url = self.base_raw_url

        base_url = self.base_url

        names: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.names, Unset):
            names = []
            for names_item_data in self.names:
                names_item = names_item_data.to_dict()
                names.append(names_item)

        options: Union[Unset, list[str]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        photo_id = self.photo_id

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if account_status is not UNSET:
            field_dict["accountStatus"] = account_status
        if base_raw_url is not UNSET:
            field_dict["baseRawUrl"] = base_raw_url
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if names is not UNSET:
            field_dict["names"] = names
        if options is not UNSET:
            field_dict["options"] = options
        if photo_id is not UNSET:
            field_dict["photoId"] = photo_id
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_name import MaxName

        d = dict(src_dict)
        id = d.pop("id")

        account_status = d.pop("accountStatus", UNSET)

        base_raw_url = d.pop("baseRawUrl", UNSET)

        base_url = d.pop("baseUrl", UNSET)

        names = []
        _names = d.pop("names", UNSET)
        for names_item_data in _names or []:
            names_item = MaxName.from_dict(names_item_data)

            names.append(names_item)

        options = cast(list[str], d.pop("options", UNSET))

        photo_id = d.pop("photoId", UNSET)

        update_time = d.pop("updateTime", UNSET)

        max_contact = cls(
            id=id,
            account_status=account_status,
            base_raw_url=base_raw_url,
            base_url=base_url,
            names=names,
            options=options,
            photo_id=photo_id,
            update_time=update_time,
        )

        max_contact.additional_properties = d
        return max_contact

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
