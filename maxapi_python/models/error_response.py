from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """The error body of every call. Most errors carry no `code`: only
    `POST /chat/send/text`, `POST /session/resume` and
    `GET /admin/users/{userid}` send one. Only `POST /chat/send/text` adds
    `upstreamCode` and the account's pause.

        Attributes:
            success (bool):
            error (str): A human-readable text, often with MAX's error inside; it may change. Do not branch on it. Example:
                send rejected: Refused: Refused (chat.denied).
            code (Union[Unset, str]): The machine code, when the answer has one. `POST /chat/send/text`:
                the delivery outcome codes `not_connected`, `invalid_target`,
                `address_not_found`, `lookup_failed`, `send_rejected`, `send_failed`
                (`address_refused` is reserved and not sent yet), and
                `INVALID_INPUT`. `POST /session/resume`: `INVALID_INPUT`,
                `INTERNAL_ERROR`. `GET /admin/users/{userid}`: `NOT_FOUND`,
                `INTERNAL_ERROR`. Treat an unknown code as a failure of the call. Example: send_rejected.
            upstream_code (Union[Unset, str]): The error code MAX itself answered with (`chat.denied`, `not.found`,
                `error.user.restricted.send`). Absent when MAX did not answer with an
                error: a timeout, a lost session, or a refusal by the gateway itself. Example: chat.denied.
            paused (Union[Unset, bool]): Present (true) only when sending from the MAX account is paused: by
                this refusal, or before it. Stop sending from every connection of
                this MAX account until `POST /session/resume`.
            pause_reason (Union[Unset, str]): Why sending from the MAX account is paused. maxapi gives only `spam` (a limit
                or restriction error of MAX). Example: spam.
    """

    success: bool
    error: str
    code: Union[Unset, str] = UNSET
    upstream_code: Union[Unset, str] = UNSET
    paused: Union[Unset, bool] = UNSET
    pause_reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        error = self.error

        code = self.code

        upstream_code = self.upstream_code

        paused = self.paused

        pause_reason = self.pause_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "error": error,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if paused is not UNSET:
            field_dict["paused"] = paused
        if pause_reason is not UNSET:
            field_dict["pauseReason"] = pause_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        error = d.pop("error")

        code = d.pop("code", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        paused = d.pop("paused", UNSET)

        pause_reason = d.pop("pauseReason", UNSET)

        error_response = cls(
            success=success,
            error=error,
            code=code,
            upstream_code=upstream_code,
            paused=paused,
            pause_reason=pause_reason,
        )

        error_response.additional_properties = d
        return error_response

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
