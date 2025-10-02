import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dipping_entry_actual_model import DippingEntryActualModel
    from ..models.dipping_entry_plan_model import DippingEntryPlanModel


T = TypeVar("T", bound="DippingEntryModel")


@_attrs_define
class DippingEntryModel:
    """Details of a dipping activity on a hole.

    Attributes:
        hole_id (int): The ID of the hole this dipping activity relates to. Cannot be edited.
        plan (DippingEntryPlanModel): Instructions on how to dip the holes.
        dipping_entry_id (Union[None, Unset, int]): The unique identifier of this dipping entry. Ignored when creating
            and editing. Cannot be edited.
        etag (Union[None, Unset, str]): The dipping entry's current ETag. Required when editing in bulk.
        created_by (Union[None, Unset, str]): Username of the person who created this dipping entry. Ignored when
            creating and editing.
        last_modified_by (Union[None, Unset, str]): Username of the person who last updated this dipping entry. Ignored
            when creating and editing.
        last_modified_time (Union[Unset, datetime.datetime]): When this dipping entry was last updated (UTC). Ignored
            when creating and editing.
        created_time (Union[None, Unset, datetime.datetime]): When this dipping entry was created (UTC). Ignored when
            editing. Defaults to current time when not supplied.
        cancelled_time (Union[None, Unset, datetime.datetime]): When this activity was cancelled (UTC). Can be null to
            indicate not cancelled. 'actual' must be null when 'cancelledTime' is not null.
        actual (Union['DippingEntryActualModel', None, Unset]): Measurements recorded from dipping the holes.
            'cancelledTime' must be null when 'actual' is not null.
    """

    hole_id: int
    plan: "DippingEntryPlanModel"
    dipping_entry_id: Union[None, Unset, int] = UNSET
    etag: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    last_modified_by: Union[None, Unset, str] = UNSET
    last_modified_time: Union[Unset, datetime.datetime] = UNSET
    created_time: Union[None, Unset, datetime.datetime] = UNSET
    cancelled_time: Union[None, Unset, datetime.datetime] = UNSET
    actual: Union["DippingEntryActualModel", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dipping_entry_actual_model import DippingEntryActualModel

        hole_id = self.hole_id

        plan = self.plan.to_dict()

        dipping_entry_id: Union[None, Unset, int]
        if isinstance(self.dipping_entry_id, Unset):
            dipping_entry_id = UNSET
        else:
            dipping_entry_id = self.dipping_entry_id

        etag: Union[None, Unset, str]
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        last_modified_by: Union[None, Unset, str]
        if isinstance(self.last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = self.last_modified_by

        last_modified_time: Union[Unset, str] = UNSET
        if self.last_modified_time and not isinstance(self.last_modified_time, Unset):
            last_modified_time = self.last_modified_time.isoformat()

        created_time: Union[None, Unset, str]
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

        cancelled_time: Union[None, Unset, str]
        if isinstance(self.cancelled_time, Unset):
            cancelled_time = UNSET
        elif isinstance(self.cancelled_time, datetime.datetime):
            cancelled_time = self.cancelled_time.isoformat()
        else:
            cancelled_time = self.cancelled_time

        actual: Union[Dict[str, Any], None, Unset]
        if isinstance(self.actual, Unset):
            actual = UNSET
        elif isinstance(self.actual, DippingEntryActualModel):
            actual = self.actual.to_dict()
        else:
            actual = self.actual

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "holeId": hole_id,
                "plan": plan,
            }
        )
        if dipping_entry_id is not UNSET:
            field_dict["dippingEntryId"] = dipping_entry_id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if last_modified_time is not UNSET:
            field_dict["lastModifiedTime"] = last_modified_time
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if cancelled_time is not UNSET:
            field_dict["cancelledTime"] = cancelled_time
        if actual is not UNSET:
            field_dict["actual"] = actual

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dipping_entry_actual_model import DippingEntryActualModel
        from ..models.dipping_entry_plan_model import DippingEntryPlanModel

        d = src_dict.copy()
        hole_id = d.pop("holeId")

        plan = DippingEntryPlanModel.from_dict(d.pop("plan"))

        def _parse_dipping_entry_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dipping_entry_id = _parse_dipping_entry_id(d.pop("dippingEntryId", UNSET))

        def _parse_etag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        def _parse_last_modified_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_modified_by = _parse_last_modified_by(d.pop("lastModifiedBy", UNSET))

        _last_modified_time = d.pop("lastModifiedTime", UNSET)
        last_modified_time: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_time, Unset):
            last_modified_time = UNSET
        else:
            last_modified_time = isoparse(_last_modified_time)

        def _parse_created_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = isoparse(data)

                return created_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_time = _parse_created_time(d.pop("createdTime", UNSET))

        def _parse_cancelled_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_time_type_0 = isoparse(data)

                return cancelled_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        cancelled_time = _parse_cancelled_time(d.pop("cancelledTime", UNSET))

        def _parse_actual(data: object) -> Union["DippingEntryActualModel", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actual_type_0 = DippingEntryActualModel.from_dict(data)

                return actual_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DippingEntryActualModel", None, Unset], data)

        actual = _parse_actual(d.pop("actual", UNSET))

        dipping_entry_model = cls(
            hole_id=hole_id,
            plan=plan,
            dipping_entry_id=dipping_entry_id,
            etag=etag,
            created_by=created_by,
            last_modified_by=last_modified_by,
            last_modified_time=last_modified_time,
            created_time=created_time,
            cancelled_time=cancelled_time,
            actual=actual,
        )

        return dipping_entry_model
