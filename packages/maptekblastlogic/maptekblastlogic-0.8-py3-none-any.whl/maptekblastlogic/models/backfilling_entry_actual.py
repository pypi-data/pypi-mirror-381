import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackfillingEntryActual")


@_attrs_define
class BackfillingEntryActual:
    """Measurements recorded from a backfilling activity.

    Attributes:
        crew_start_time (datetime.datetime): When this backfilling activity started (UTC).
        crew_end_time (datetime.datetime): When this backfilling activity was completed (UTC). Must be greater than or
            equal to 'crewStartTime'.
        crew_id (Union[None, Unset, int]): The unique identifier of the crew that performed this backfilling. Can be
            null if unknown.
        crew_dip_depth_before (Union[None, Unset, float]): Depth of the hole before backfilling according to the crew
            (Meters). Can be null if unknown.
        crew_water_length_before (Union[None, Unset, float]): Depth of the water in the hole before backfilling
            according to the crew (Meters). Can be null if unknown.
        crew_wet_sides_length_before (Union[None, Unset, float]): Length of the wet sides of the hole before backfilling
            according to the crew (Meters). Can be null if unknown.
        crew_temperature_before (Union[None, Unset, float]): Temperature of the hole before backfilling according to the
            crew (Kelvin). Can be null if unknown.
        was_backfilled (Union[None, Unset, bool]): Whether or not the hole was backfilled.
        crew_dip_depth_after (Union[None, Unset, float]): Depth of the hole after backfilling according to the crew
            (Meters). Must be null when 'wasBackfilled' is false. Can be null if unknown.
        crew_water_length_after (Union[None, Unset, float]): Depth of the water in the hole after backfilling according
            to the crew (Meters). Must be null when 'wasBackfilled' is false. Can be null if unknown.
        crew_wet_sides_length_after (Union[None, Unset, float]): Length of the wet sides of the hole after backfilling
            according to the crew (Meters). Must be null when 'wasBackfilled' is false. Can be null if unknown.
        crew_comment (Union[None, Unset, str]): Comments about the hole during the backfilling activity. Can be null.
            Maximum 200 characters.
        supervisor_id (Union[None, Unset, int]): The unique identifier of the supervisor responsible for supervising
            this backfilling activity. Can be null if unknown.
        supervisor_start_time (Union[None, Unset, datetime.datetime]): When the supervisor checked started (UTC).
            Required when 'supervisorEndTime' has a value.
        supervisor_end_time (Union[None, Unset, datetime.datetime]): When the supervisor checked finished (UTC).
            Required when 'supervisorStartTime' has a value.
        supervisor_dip_depth_after (Union[None, Unset, float]): Depth of the hole after backfilling according to the
            supervisor (Meters). Can be null if unknown.
        supervisor_water_length_after (Union[None, Unset, float]): Depth of water in the hole after backfilling
            according to the supervisor (Meters). Can be null if unknown.
        supervisor_wet_sides_length_after (Union[None, Unset, float]): Length of the wet sides in the hole after
            backfilling according to the supervisor (Meters). Can be null if unknown.
    """

    crew_start_time: datetime.datetime
    crew_end_time: datetime.datetime
    crew_id: Union[None, Unset, int] = UNSET
    crew_dip_depth_before: Union[None, Unset, float] = UNSET
    crew_water_length_before: Union[None, Unset, float] = UNSET
    crew_wet_sides_length_before: Union[None, Unset, float] = UNSET
    crew_temperature_before: Union[None, Unset, float] = UNSET
    was_backfilled: Union[None, Unset, bool] = UNSET
    crew_dip_depth_after: Union[None, Unset, float] = UNSET
    crew_water_length_after: Union[None, Unset, float] = UNSET
    crew_wet_sides_length_after: Union[None, Unset, float] = UNSET
    crew_comment: Union[None, Unset, str] = UNSET
    supervisor_id: Union[None, Unset, int] = UNSET
    supervisor_start_time: Union[None, Unset, datetime.datetime] = UNSET
    supervisor_end_time: Union[None, Unset, datetime.datetime] = UNSET
    supervisor_dip_depth_after: Union[None, Unset, float] = UNSET
    supervisor_water_length_after: Union[None, Unset, float] = UNSET
    supervisor_wet_sides_length_after: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        crew_start_time = self.crew_start_time.isoformat()

        crew_end_time = self.crew_end_time.isoformat()

        crew_id: Union[None, Unset, int]
        if isinstance(self.crew_id, Unset):
            crew_id = UNSET
        else:
            crew_id = self.crew_id

        crew_dip_depth_before: Union[None, Unset, float]
        if isinstance(self.crew_dip_depth_before, Unset):
            crew_dip_depth_before = UNSET
        else:
            crew_dip_depth_before = self.crew_dip_depth_before

        crew_water_length_before: Union[None, Unset, float]
        if isinstance(self.crew_water_length_before, Unset):
            crew_water_length_before = UNSET
        else:
            crew_water_length_before = self.crew_water_length_before

        crew_wet_sides_length_before: Union[None, Unset, float]
        if isinstance(self.crew_wet_sides_length_before, Unset):
            crew_wet_sides_length_before = UNSET
        else:
            crew_wet_sides_length_before = self.crew_wet_sides_length_before

        crew_temperature_before: Union[None, Unset, float]
        if isinstance(self.crew_temperature_before, Unset):
            crew_temperature_before = UNSET
        else:
            crew_temperature_before = self.crew_temperature_before

        was_backfilled: Union[None, Unset, bool]
        if isinstance(self.was_backfilled, Unset):
            was_backfilled = UNSET
        else:
            was_backfilled = self.was_backfilled

        crew_dip_depth_after: Union[None, Unset, float]
        if isinstance(self.crew_dip_depth_after, Unset):
            crew_dip_depth_after = UNSET
        else:
            crew_dip_depth_after = self.crew_dip_depth_after

        crew_water_length_after: Union[None, Unset, float]
        if isinstance(self.crew_water_length_after, Unset):
            crew_water_length_after = UNSET
        else:
            crew_water_length_after = self.crew_water_length_after

        crew_wet_sides_length_after: Union[None, Unset, float]
        if isinstance(self.crew_wet_sides_length_after, Unset):
            crew_wet_sides_length_after = UNSET
        else:
            crew_wet_sides_length_after = self.crew_wet_sides_length_after

        crew_comment: Union[None, Unset, str]
        if isinstance(self.crew_comment, Unset):
            crew_comment = UNSET
        else:
            crew_comment = self.crew_comment

        supervisor_id: Union[None, Unset, int]
        if isinstance(self.supervisor_id, Unset):
            supervisor_id = UNSET
        else:
            supervisor_id = self.supervisor_id

        supervisor_start_time: Union[None, Unset, str]
        if isinstance(self.supervisor_start_time, Unset):
            supervisor_start_time = UNSET
        elif isinstance(self.supervisor_start_time, datetime.datetime):
            supervisor_start_time = self.supervisor_start_time.isoformat()
        else:
            supervisor_start_time = self.supervisor_start_time

        supervisor_end_time: Union[None, Unset, str]
        if isinstance(self.supervisor_end_time, Unset):
            supervisor_end_time = UNSET
        elif isinstance(self.supervisor_end_time, datetime.datetime):
            supervisor_end_time = self.supervisor_end_time.isoformat()
        else:
            supervisor_end_time = self.supervisor_end_time

        supervisor_dip_depth_after: Union[None, Unset, float]
        if isinstance(self.supervisor_dip_depth_after, Unset):
            supervisor_dip_depth_after = UNSET
        else:
            supervisor_dip_depth_after = self.supervisor_dip_depth_after

        supervisor_water_length_after: Union[None, Unset, float]
        if isinstance(self.supervisor_water_length_after, Unset):
            supervisor_water_length_after = UNSET
        else:
            supervisor_water_length_after = self.supervisor_water_length_after

        supervisor_wet_sides_length_after: Union[None, Unset, float]
        if isinstance(self.supervisor_wet_sides_length_after, Unset):
            supervisor_wet_sides_length_after = UNSET
        else:
            supervisor_wet_sides_length_after = self.supervisor_wet_sides_length_after

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "crewStartTime": crew_start_time,
                "crewEndTime": crew_end_time,
            }
        )
        if crew_id is not UNSET:
            field_dict["crewId"] = crew_id
        if crew_dip_depth_before is not UNSET:
            field_dict["crewDipDepthBefore"] = crew_dip_depth_before
        if crew_water_length_before is not UNSET:
            field_dict["crewWaterLengthBefore"] = crew_water_length_before
        if crew_wet_sides_length_before is not UNSET:
            field_dict["crewWetSidesLengthBefore"] = crew_wet_sides_length_before
        if crew_temperature_before is not UNSET:
            field_dict["crewTemperatureBefore"] = crew_temperature_before
        if was_backfilled is not UNSET:
            field_dict["wasBackfilled"] = was_backfilled
        if crew_dip_depth_after is not UNSET:
            field_dict["crewDipDepthAfter"] = crew_dip_depth_after
        if crew_water_length_after is not UNSET:
            field_dict["crewWaterLengthAfter"] = crew_water_length_after
        if crew_wet_sides_length_after is not UNSET:
            field_dict["crewWetSidesLengthAfter"] = crew_wet_sides_length_after
        if crew_comment is not UNSET:
            field_dict["crewComment"] = crew_comment
        if supervisor_id is not UNSET:
            field_dict["supervisorId"] = supervisor_id
        if supervisor_start_time is not UNSET:
            field_dict["supervisorStartTime"] = supervisor_start_time
        if supervisor_end_time is not UNSET:
            field_dict["supervisorEndTime"] = supervisor_end_time
        if supervisor_dip_depth_after is not UNSET:
            field_dict["supervisorDipDepthAfter"] = supervisor_dip_depth_after
        if supervisor_water_length_after is not UNSET:
            field_dict["supervisorWaterLengthAfter"] = supervisor_water_length_after
        if supervisor_wet_sides_length_after is not UNSET:
            field_dict["supervisorWetSidesLengthAfter"] = supervisor_wet_sides_length_after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        crew_start_time = isoparse(d.pop("crewStartTime"))

        crew_end_time = isoparse(d.pop("crewEndTime"))

        def _parse_crew_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        crew_id = _parse_crew_id(d.pop("crewId", UNSET))

        def _parse_crew_dip_depth_before(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_dip_depth_before = _parse_crew_dip_depth_before(d.pop("crewDipDepthBefore", UNSET))

        def _parse_crew_water_length_before(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_water_length_before = _parse_crew_water_length_before(d.pop("crewWaterLengthBefore", UNSET))

        def _parse_crew_wet_sides_length_before(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_wet_sides_length_before = _parse_crew_wet_sides_length_before(d.pop("crewWetSidesLengthBefore", UNSET))

        def _parse_crew_temperature_before(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_temperature_before = _parse_crew_temperature_before(d.pop("crewTemperatureBefore", UNSET))

        def _parse_was_backfilled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        was_backfilled = _parse_was_backfilled(d.pop("wasBackfilled", UNSET))

        def _parse_crew_dip_depth_after(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_dip_depth_after = _parse_crew_dip_depth_after(d.pop("crewDipDepthAfter", UNSET))

        def _parse_crew_water_length_after(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_water_length_after = _parse_crew_water_length_after(d.pop("crewWaterLengthAfter", UNSET))

        def _parse_crew_wet_sides_length_after(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_wet_sides_length_after = _parse_crew_wet_sides_length_after(d.pop("crewWetSidesLengthAfter", UNSET))

        def _parse_crew_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        crew_comment = _parse_crew_comment(d.pop("crewComment", UNSET))

        def _parse_supervisor_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        supervisor_id = _parse_supervisor_id(d.pop("supervisorId", UNSET))

        def _parse_supervisor_start_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                supervisor_start_time_type_0 = isoparse(data)

                return supervisor_start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        supervisor_start_time = _parse_supervisor_start_time(d.pop("supervisorStartTime", UNSET))

        def _parse_supervisor_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                supervisor_end_time_type_0 = isoparse(data)

                return supervisor_end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        supervisor_end_time = _parse_supervisor_end_time(d.pop("supervisorEndTime", UNSET))

        def _parse_supervisor_dip_depth_after(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supervisor_dip_depth_after = _parse_supervisor_dip_depth_after(d.pop("supervisorDipDepthAfter", UNSET))

        def _parse_supervisor_water_length_after(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supervisor_water_length_after = _parse_supervisor_water_length_after(d.pop("supervisorWaterLengthAfter", UNSET))

        def _parse_supervisor_wet_sides_length_after(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supervisor_wet_sides_length_after = _parse_supervisor_wet_sides_length_after(
            d.pop("supervisorWetSidesLengthAfter", UNSET)
        )

        backfilling_entry_actual = cls(
            crew_start_time=crew_start_time,
            crew_end_time=crew_end_time,
            crew_id=crew_id,
            crew_dip_depth_before=crew_dip_depth_before,
            crew_water_length_before=crew_water_length_before,
            crew_wet_sides_length_before=crew_wet_sides_length_before,
            crew_temperature_before=crew_temperature_before,
            was_backfilled=was_backfilled,
            crew_dip_depth_after=crew_dip_depth_after,
            crew_water_length_after=crew_water_length_after,
            crew_wet_sides_length_after=crew_wet_sides_length_after,
            crew_comment=crew_comment,
            supervisor_id=supervisor_id,
            supervisor_start_time=supervisor_start_time,
            supervisor_end_time=supervisor_end_time,
            supervisor_dip_depth_after=supervisor_dip_depth_after,
            supervisor_water_length_after=supervisor_water_length_after,
            supervisor_wet_sides_length_after=supervisor_wet_sides_length_after,
        )

        return backfilling_entry_actual
