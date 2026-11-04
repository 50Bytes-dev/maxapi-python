from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.max_name import MaxName


T = TypeVar("T", bound="MaxUserInfo")


@_attrs_define
class MaxUserInfo:
    """A MAX user. Every field is present; `names` and `options` may be null.

    Attributes:
        id (int):  Example: 987654321.
        account_status (int):
        names (Union[None, list['MaxName']]):
        options (Union[None, list[str]]):
        base_url (str):
        base_raw_url (str):
        photo_id (int):
        description (str):
        gender (int):
        link (str):
        update_time (int):
        web_app (str):
        avatar_url (str): `baseRawUrl`, else `baseUrl`; "" when neither
    """

    id: int
    account_status: int
    names: Union[None, list["MaxName"]]
    options: Union[None, list[str]]
    base_url: str
    base_raw_url: str
    photo_id: int
    description: str
    gender: int
    link: str
    update_time: int
    web_app: str
    avatar_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_status = self.account_status

        names: Union[None, list[dict[str, Any]]]
        if isinstance(self.names, list):
            names = []
            for names_type_0_item_data in self.names:
                names_type_0_item = names_type_0_item_data.to_dict()
                names.append(names_type_0_item)

        else:
            names = self.names

        options: Union[None, list[str]]
        if isinstance(self.options, list):
            options = self.options

        else:
            options = self.options

        base_url = self.base_url

        base_raw_url = self.base_raw_url

        photo_id = self.photo_id

        description = self.description

        gender = self.gender

        link = self.link

        update_time = self.update_time

        web_app = self.web_app

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "accountStatus": account_status,
                "names": names,
                "options": options,
                "baseUrl": base_url,
                "baseRawUrl": base_raw_url,
                "photoId": photo_id,
                "description": description,
                "gender": gender,
                "link": link,
                "updateTime": update_time,
                "webApp": web_app,
                "avatarUrl": avatar_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_name import MaxName

        d = dict(src_dict)
        id = d.pop("id")

        account_status = d.pop("accountStatus")

        def _parse_names(data: object) -> Union[None, list["MaxName"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                names_type_0 = []
                _names_type_0 = data
                for names_type_0_item_data in _names_type_0:
                    names_type_0_item = MaxName.from_dict(names_type_0_item_data)

                    names_type_0.append(names_type_0_item)

                return names_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["MaxName"]], data)

        names = _parse_names(d.pop("names"))

        def _parse_options(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(list[str], data)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        options = _parse_options(d.pop("options"))

        base_url = d.pop("baseUrl")

        base_raw_url = d.pop("baseRawUrl")

        photo_id = d.pop("photoId")

        description = d.pop("description")

        gender = d.pop("gender")

        link = d.pop("link")

        update_time = d.pop("updateTime")

        web_app = d.pop("webApp")

        avatar_url = d.pop("avatarUrl")

        max_user_info = cls(
            id=id,
            account_status=account_status,
            names=names,
            options=options,
            base_url=base_url,
            base_raw_url=base_raw_url,
            photo_id=photo_id,
            description=description,
            gender=gender,
            link=link,
            update_time=update_time,
            web_app=web_app,
            avatar_url=avatar_url,
        )

        max_user_info.additional_properties = d
        return max_user_info

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
