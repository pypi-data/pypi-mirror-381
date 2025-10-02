import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.blast_status import BlastStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BlastModel")


@_attrs_define
class BlastModel:
    """A collection of holes designed to be detonated together.

    Attributes:
        blast_name (str): The name of this blast.
        blast_id (Union[Unset, int]): The unique identifier of this blast.
        status (Union[Unset, BlastStatus]):
        fired_time (Union[None, Unset, datetime.datetime]): When this blast was fired (UTC). Null indicates the blast
            has not been fired.
        abandoned_time (Union[None, Unset, datetime.datetime]): When this blast was abandoned (UTC). Null indicates the
            blast has not been abandoned.
    """

    blast_name: str
    blast_id: Union[Unset, int] = UNSET
    status: Union[Unset, BlastStatus] = UNSET
    fired_time: Union[None, Unset, datetime.datetime] = UNSET
    abandoned_time: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        blast_name = self.blast_name

        blast_id = self.blast_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        fired_time: Union[None, Unset, str]
        if isinstance(self.fired_time, Unset):
            fired_time = UNSET
        elif isinstance(self.fired_time, datetime.datetime):
            fired_time = self.fired_time.isoformat()
        else:
            fired_time = self.fired_time

        abandoned_time: Union[None, Unset, str]
        if isinstance(self.abandoned_time, Unset):
            abandoned_time = UNSET
        elif isinstance(self.abandoned_time, datetime.datetime):
            abandoned_time = self.abandoned_time.isoformat()
        else:
            abandoned_time = self.abandoned_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "blastName": blast_name,
            }
        )
        if blast_id is not UNSET:
            field_dict["blastId"] = blast_id
        if status is not UNSET:
            field_dict["status"] = status
        if fired_time is not UNSET:
            field_dict["firedTime"] = fired_time
        if abandoned_time is not UNSET:
            field_dict["abandonedTime"] = abandoned_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        blast_name = d.pop("blastName")

        blast_id = d.pop("blastId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BlastStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BlastStatus(_status)

        def _parse_fired_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fired_time_type_0 = isoparse(data)

                return fired_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        fired_time = _parse_fired_time(d.pop("firedTime", UNSET))

        def _parse_abandoned_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                abandoned_time_type_0 = isoparse(data)

                return abandoned_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        abandoned_time = _parse_abandoned_time(d.pop("abandonedTime", UNSET))

        blast_model = cls(
            blast_name=blast_name,
            blast_id=blast_id,
            status=status,
            fired_time=fired_time,
            abandoned_time=abandoned_time,
        )

        return blast_model
