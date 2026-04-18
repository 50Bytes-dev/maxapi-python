from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """Snapshot of process + connection health.

    Attributes:
        connected_users (Union[Unset, int]):  Example: 42.
        db_ok (Union[Unset, bool]):  Example: True.
        goroutines (Union[Unset, int]):  Example: 87.
        mem_alloc_mb (Union[Unset, int]):  Example: 67.
        rabbitmq_ok (Union[Unset, bool]):  Example: True.
        status (Union[Unset, str]):  Example: ok.
        success (Union[Unset, bool]):  Example: True.
        timestamp (Union[Unset, int]):  Example: 1700000000.
        uptime_seconds (Union[Unset, int]):  Example: 12345.
        version (Union[Unset, str]):  Example: 2.0.0-max.
    """

    connected_users: Union[Unset, int] = UNSET
    db_ok: Union[Unset, bool] = UNSET
    goroutines: Union[Unset, int] = UNSET
    mem_alloc_mb: Union[Unset, int] = UNSET
    rabbitmq_ok: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    timestamp: Union[Unset, int] = UNSET
    uptime_seconds: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_users = self.connected_users

        db_ok = self.db_ok

        goroutines = self.goroutines

        mem_alloc_mb = self.mem_alloc_mb

        rabbitmq_ok = self.rabbitmq_ok

        status = self.status

        success = self.success

        timestamp = self.timestamp

        uptime_seconds = self.uptime_seconds

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_users is not UNSET:
            field_dict["connected_users"] = connected_users
        if db_ok is not UNSET:
            field_dict["db_ok"] = db_ok
        if goroutines is not UNSET:
            field_dict["goroutines"] = goroutines
        if mem_alloc_mb is not UNSET:
            field_dict["mem_alloc_mb"] = mem_alloc_mb
        if rabbitmq_ok is not UNSET:
            field_dict["rabbitmq_ok"] = rabbitmq_ok
        if status is not UNSET:
            field_dict["status"] = status
        if success is not UNSET:
            field_dict["success"] = success
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if uptime_seconds is not UNSET:
            field_dict["uptime_seconds"] = uptime_seconds
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected_users = d.pop("connected_users", UNSET)

        db_ok = d.pop("db_ok", UNSET)

        goroutines = d.pop("goroutines", UNSET)

        mem_alloc_mb = d.pop("mem_alloc_mb", UNSET)

        rabbitmq_ok = d.pop("rabbitmq_ok", UNSET)

        status = d.pop("status", UNSET)

        success = d.pop("success", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        uptime_seconds = d.pop("uptime_seconds", UNSET)

        version = d.pop("version", UNSET)

        health_response = cls(
            connected_users=connected_users,
            db_ok=db_ok,
            goroutines=goroutines,
            mem_alloc_mb=mem_alloc_mb,
            rabbitmq_ok=rabbitmq_ok,
            status=status,
            success=success,
            timestamp=timestamp,
            uptime_seconds=uptime_seconds,
            version=version,
        )

        health_response.additional_properties = d
        return health_response

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
