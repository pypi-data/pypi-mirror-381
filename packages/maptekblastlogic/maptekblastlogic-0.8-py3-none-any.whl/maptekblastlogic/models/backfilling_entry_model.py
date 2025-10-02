import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backfilling_entry_actual import BackfillingEntryActual
    from ..models.backfilling_entry_plan import BackfillingEntryPlan


T = TypeVar("T", bound="BackfillingEntryModel")


@_attrs_define
class BackfillingEntryModel:
    """Details of a backfilling activity on a hole.

    Attributes:
        hole_id (int): The ID of the hole this backfilling activity relates to. Cannot be edited.
        plan (BackfillingEntryPlan): Instructions on how a backfilling activity should be performed.
        backfilling_entry_id (Union[None, Unset, int]): The unique identifier of this backfilling entry. Ignored when
            creating. Cannot be edited.
        etag (Union[None, Unset, str]): The backfilling entry's current ETag. Required when editing in bulk.
        created_by (Union[None, Unset, str]): Username of the person who created this backfilling entry. Ignored when
            creating and editing.
        last_modified_by (Union[None, Unset, str]): Username of the person who last updated this backfilling entry.
            Ignored when creating and editing.
        last_modified_time (Union[None, Unset, datetime.datetime]): When this backfilling entry was last updated (UTC).
            Ignored when creating and editing.
        created_time (Union[None, Unset, datetime.datetime]): When this backfilling entry was created (UTC). Ignored
            when editing. Defaults to current time when not supplied.
        cancelled_time (Union[None, Unset, datetime.datetime]): When this activity was cancelled (UTC). Can be null to
            indicate not cancelled. 'actual' must be null when 'cancelledTime' is not null.
        actual (Union['BackfillingEntryActual', None, Unset]): Measurements recorded from the backfilling activity.
            'cancelledTime' must be null when 'actual' is not null.
    """

    hole_id: int
    plan: "BackfillingEntryPlan"
    backfilling_entry_id: Union[None, Unset, int] = UNSET
    etag: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    last_modified_by: Union[None, Unset, str] = UNSET
    last_modified_time: Union[None, Unset, datetime.datetime] = UNSET
    created_time: Union[None, Unset, datetime.datetime] = UNSET
    cancelled_time: Union[None, Unset, datetime.datetime] = UNSET
    actual: Union["BackfillingEntryActual", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.backfilling_entry_actual import BackfillingEntryActual

        hole_id = self.hole_id

        plan = self.plan.to_dict()

        backfilling_entry_id: Union[None, Unset, int]
        if isinstance(self.backfilling_entry_id, Unset):
            backfilling_entry_id = UNSET
        else:
            backfilling_entry_id = self.backfilling_entry_id

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

        last_modified_time: Union[None, Unset, str]
        if isinstance(self.last_modified_time, Unset):
            last_modified_time = UNSET
        elif isinstance(self.last_modified_time, datetime.datetime):
            last_modified_time = self.last_modified_time.isoformat()
        else:
            last_modified_time = self.last_modified_time

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
        elif isinstance(self.actual, BackfillingEntryActual):
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
        if backfilling_entry_id is not UNSET:
            field_dict["backfillingEntryId"] = backfilling_entry_id
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
        from ..models.backfilling_entry_actual import BackfillingEntryActual
        from ..models.backfilling_entry_plan import BackfillingEntryPlan

        d = src_dict.copy()
        hole_id = d.pop("holeId")

        plan = BackfillingEntryPlan.from_dict(d.pop("plan"))

        def _parse_backfilling_entry_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backfilling_entry_id = _parse_backfilling_entry_id(d.pop("backfillingEntryId", UNSET))

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

        def _parse_last_modified_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_time_type_0 = isoparse(data)

                return last_modified_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_modified_time = _parse_last_modified_time(d.pop("lastModifiedTime", UNSET))

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

        def _parse_actual(data: object) -> Union["BackfillingEntryActual", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actual_type_0 = BackfillingEntryActual.from_dict(data)

                return actual_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackfillingEntryActual", None, Unset], data)

        actual = _parse_actual(d.pop("actual", UNSET))

        backfilling_entry_model = cls(
            hole_id=hole_id,
            plan=plan,
            backfilling_entry_id=backfilling_entry_id,
            etag=etag,
            created_by=created_by,
            last_modified_by=last_modified_by,
            last_modified_time=last_modified_time,
            created_time=created_time,
            cancelled_time=cancelled_time,
            actual=actual,
        )

        return backfilling_entry_model
