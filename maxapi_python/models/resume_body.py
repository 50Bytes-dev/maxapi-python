from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResumeBody")


@_attrs_define
class ResumeBody:
    """Optional; no body and `{}` work too.

    Attributes:
        captcha_key (Union[Unset, str]): Part of the VK gateway's contract; read and ignored (a MAX pause has no
            captcha).
    """

    captcha_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        captcha_key = self.captcha_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if captcha_key is not UNSET:
            field_dict["captchaKey"] = captcha_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        captcha_key = d.pop("captchaKey", UNSET)

        resume_body = cls(
            captcha_key=captcha_key,
        )

        resume_body.additional_properties = d
        return resume_body

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
