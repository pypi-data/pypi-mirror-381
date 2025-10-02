import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonModel")


@_attrs_define
class PersonModel:
    """A person and their responsibilities.

    Attributes:
        personnel_id (Union[Unset, int]): The unique identifier of this person.
        etag (Union[None, Unset, str]): The person's ETag. Ignored when creating and editing.
        created_by (Union[None, Unset, str]): Username of the person who created this person. Ignored when creating and
            editing.
        created_time (Union[None, Unset, datetime.datetime]): When this person was last updated (UTC). Ignored when
            creating and editing.
        last_modified_by (Union[None, Unset, str]): Username of the person who last updated this person. Ignored when
            creating and editing.
        last_modified_time (Union[None, Unset, datetime.datetime]): When this person was last updated (UTC). Ignored
            when creating and editing.
        name (Union[None, Unset, str]): The name of this person.
        is_backfilling_supervisor (Union[Unset, bool]): Whether this person can supervise backfilling activities.
        is_dipping_supervisor (Union[Unset, bool]): Whether this person can supervise dipping activities.
        is_loading_truck_operator (Union[Unset, bool]): Whether this person can operate loading trucks.
        is_shot_firer (Union[Unset, bool]): Whether this person can perform shotfirer duties.
    """

    personnel_id: Union[Unset, int] = UNSET
    etag: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    created_time: Union[None, Unset, datetime.datetime] = UNSET
    last_modified_by: Union[None, Unset, str] = UNSET
    last_modified_time: Union[None, Unset, datetime.datetime] = UNSET
    name: Union[None, Unset, str] = UNSET
    is_backfilling_supervisor: Union[Unset, bool] = UNSET
    is_dipping_supervisor: Union[Unset, bool] = UNSET
    is_loading_truck_operator: Union[Unset, bool] = UNSET
    is_shot_firer: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        personnel_id = self.personnel_id

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

        created_time: Union[None, Unset, str]
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

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

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_backfilling_supervisor = self.is_backfilling_supervisor

        is_dipping_supervisor = self.is_dipping_supervisor

        is_loading_truck_operator = self.is_loading_truck_operator

        is_shot_firer = self.is_shot_firer

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if personnel_id is not UNSET:
            field_dict["personnelId"] = personnel_id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if last_modified_time is not UNSET:
            field_dict["lastModifiedTime"] = last_modified_time
        if name is not UNSET:
            field_dict["name"] = name
        if is_backfilling_supervisor is not UNSET:
            field_dict["isBackfillingSupervisor"] = is_backfilling_supervisor
        if is_dipping_supervisor is not UNSET:
            field_dict["isDippingSupervisor"] = is_dipping_supervisor
        if is_loading_truck_operator is not UNSET:
            field_dict["isLoadingTruckOperator"] = is_loading_truck_operator
        if is_shot_firer is not UNSET:
            field_dict["isShotFirer"] = is_shot_firer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        personnel_id = d.pop("personnelId", UNSET)

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        is_backfilling_supervisor = d.pop("isBackfillingSupervisor", UNSET)

        is_dipping_supervisor = d.pop("isDippingSupervisor", UNSET)

        is_loading_truck_operator = d.pop("isLoadingTruckOperator", UNSET)

        is_shot_firer = d.pop("isShotFirer", UNSET)

        person_model = cls(
            personnel_id=personnel_id,
            etag=etag,
            created_by=created_by,
            created_time=created_time,
            last_modified_by=last_modified_by,
            last_modified_time=last_modified_time,
            name=name,
            is_backfilling_supervisor=is_backfilling_supervisor,
            is_dipping_supervisor=is_dipping_supervisor,
            is_loading_truck_operator=is_loading_truck_operator,
            is_shot_firer=is_shot_firer,
        )

        return person_model
