from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """The error body of every call. On every account call that reaches MAX it
    carries a machine `code`; the codes are listed in API.md, "Codes", each
    with its HTTP status. `upstreamCode` is MAX's own code, present whenever
    MAX answered with an error. A failure because of the account's pause
    carries `paused` and `pauseReason`.

        Attributes:
            success (bool):
            error (str): A human-readable text; it may change. Do not branch on it. Example: MAX refused the message.
            code (Union[Unset, str]): The machine code. Delivery (a send, a delete): `not_connected`,
                `invalid_target`, `address_not_found`, `address_refused`,
                `lookup_failed`, `send_rejected`, `message_rejected`,
                `attachment_rejected`, `send_failed`. Other calls that reach MAX:
                `page_paused`, `upstream_error`, `not_connected`. Media:
                `invalid_image`, `fetch_failed`, `upload_failed`. Generic:
                `INVALID_INPUT`, `INTERNAL_ERROR`, `NOT_FOUND`. Treat an unknown code
                as a failure of the call. Example: send_rejected.
            upstream_code (Union[Unset, str]): MAX's own error code (`chat.denied`, `not.found`,
                `error.user.restricted.send`), present whenever MAX answered with
                an error. Absent when no MAX call was made (a pause that was
                already set) or MAX did not answer. Example: chat.denied.
            paused (Union[Unset, bool]): Present (true) only when the MAX account is paused: by this refusal,
                or before it. Until `POST /session/resume`, every gateway account of
                this MAX account is refused what acts in MAX (sends, deletes, edits,
                reactions, uploads, phone lookups, group changes); reads go on.
            pause_reason (Union[Unset, str]): Why the MAX account is paused. maxapi gives only `spam` (a limit or
                restriction error of MAX). Example: spam.
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
