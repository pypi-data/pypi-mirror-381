import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DippingEntryActualModel")


@_attrs_define
class DippingEntryActualModel:
    """Measurements recorded from dipping holes.

    Attributes:
        crew_start_time (datetime.datetime): When the crew stared dipping (UTC).
        crew_end_time (datetime.datetime): When the crew completed dipping (UTC). Must be greater than or equal to
            'crewStartTime'.
        crew_id (Union[None, Unset, int]): Id of the crew that performed the dipping activity. Can be null if unknown.
        crew_depth (Union[None, Unset, float]): Depth of the hole according to the crew (Meters). Can be null if
            unknown.
        crew_water_length (Union[None, Unset, float]): Depth of the water in the hole according to the crew (Meters).
            Can be null if unknown.
        crew_wet_sides_length (Union[None, Unset, float]): Length of the wet sides in the hole according to the crew
            (Meters). Can be null if unknown.
        crew_temperature (Union[None, Unset, float]): Temperature of the hole according to the crew (Kelvin). Can be
            null if unknown.
        crew_comment (Union[None, Unset, str]): Comments about the hole during the dipping activity. Can be null.
        supervisor_id (Union[None, Unset, int]): Id of the person responsible for supervising this dipping activity. Can
            be null if unknown.
        supervisor_start_time (Union[None, Unset, datetime.datetime]): When the supervisor check started (UTC). Cannot
            be null if 'supervisorEndTime' is not null.
        supervisor_end_time (Union[None, Unset, datetime.datetime]): When the supervisor check finished (UTC). Cannot be
            null if 'supervisorStartTime' is not null. If not null, must be greater than or equal to 'supervisorStartTime'.
        supervisor_depth (Union[None, Unset, float]): Depth of the hole according to the supervisor (Meters). Can be
            null if unknown.
        supervisor_water_length (Union[None, Unset, float]): Length of the wet sides of the hole according to the
            supervisor (Meters). Can be null if unknown.
        supervisor_wet_sides_length (Union[None, Unset, float]): Length of the wet sides in the hole according to the
            supervisor (Meters). Can be null if unknown.
    """

    crew_start_time: datetime.datetime
    crew_end_time: datetime.datetime
    crew_id: Union[None, Unset, int] = UNSET
    crew_depth: Union[None, Unset, float] = UNSET
    crew_water_length: Union[None, Unset, float] = UNSET
    crew_wet_sides_length: Union[None, Unset, float] = UNSET
    crew_temperature: Union[None, Unset, float] = UNSET
    crew_comment: Union[None, Unset, str] = UNSET
    supervisor_id: Union[None, Unset, int] = UNSET
    supervisor_start_time: Union[None, Unset, datetime.datetime] = UNSET
    supervisor_end_time: Union[None, Unset, datetime.datetime] = UNSET
    supervisor_depth: Union[None, Unset, float] = UNSET
    supervisor_water_length: Union[None, Unset, float] = UNSET
    supervisor_wet_sides_length: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        crew_start_time = self.crew_start_time.isoformat()

        crew_end_time = self.crew_end_time.isoformat()

        crew_id: Union[None, Unset, int]
        if isinstance(self.crew_id, Unset):
            crew_id = UNSET
        else:
            crew_id = self.crew_id

        crew_depth: Union[None, Unset, float]
        if isinstance(self.crew_depth, Unset):
            crew_depth = UNSET
        else:
            crew_depth = self.crew_depth

        crew_water_length: Union[None, Unset, float]
        if isinstance(self.crew_water_length, Unset):
            crew_water_length = UNSET
        else:
            crew_water_length = self.crew_water_length

        crew_wet_sides_length: Union[None, Unset, float]
        if isinstance(self.crew_wet_sides_length, Unset):
            crew_wet_sides_length = UNSET
        else:
            crew_wet_sides_length = self.crew_wet_sides_length

        crew_temperature: Union[None, Unset, float]
        if isinstance(self.crew_temperature, Unset):
            crew_temperature = UNSET
        else:
            crew_temperature = self.crew_temperature

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

        supervisor_depth: Union[None, Unset, float]
        if isinstance(self.supervisor_depth, Unset):
            supervisor_depth = UNSET
        else:
            supervisor_depth = self.supervisor_depth

        supervisor_water_length: Union[None, Unset, float]
        if isinstance(self.supervisor_water_length, Unset):
            supervisor_water_length = UNSET
        else:
            supervisor_water_length = self.supervisor_water_length

        supervisor_wet_sides_length: Union[None, Unset, float]
        if isinstance(self.supervisor_wet_sides_length, Unset):
            supervisor_wet_sides_length = UNSET
        else:
            supervisor_wet_sides_length = self.supervisor_wet_sides_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "crewStartTime": crew_start_time,
                "crewEndTime": crew_end_time,
            }
        )
        if crew_id is not UNSET:
            field_dict["crewId"] = crew_id
        if crew_depth is not UNSET:
            field_dict["crewDepth"] = crew_depth
        if crew_water_length is not UNSET:
            field_dict["crewWaterLength"] = crew_water_length
        if crew_wet_sides_length is not UNSET:
            field_dict["crewWetSidesLength"] = crew_wet_sides_length
        if crew_temperature is not UNSET:
            field_dict["crewTemperature"] = crew_temperature
        if crew_comment is not UNSET:
            field_dict["crewComment"] = crew_comment
        if supervisor_id is not UNSET:
            field_dict["supervisorId"] = supervisor_id
        if supervisor_start_time is not UNSET:
            field_dict["supervisorStartTime"] = supervisor_start_time
        if supervisor_end_time is not UNSET:
            field_dict["supervisorEndTime"] = supervisor_end_time
        if supervisor_depth is not UNSET:
            field_dict["supervisorDepth"] = supervisor_depth
        if supervisor_water_length is not UNSET:
            field_dict["supervisorWaterLength"] = supervisor_water_length
        if supervisor_wet_sides_length is not UNSET:
            field_dict["supervisorWetSidesLength"] = supervisor_wet_sides_length

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

        def _parse_crew_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_depth = _parse_crew_depth(d.pop("crewDepth", UNSET))

        def _parse_crew_water_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_water_length = _parse_crew_water_length(d.pop("crewWaterLength", UNSET))

        def _parse_crew_wet_sides_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_wet_sides_length = _parse_crew_wet_sides_length(d.pop("crewWetSidesLength", UNSET))

        def _parse_crew_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        crew_temperature = _parse_crew_temperature(d.pop("crewTemperature", UNSET))

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

        def _parse_supervisor_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supervisor_depth = _parse_supervisor_depth(d.pop("supervisorDepth", UNSET))

        def _parse_supervisor_water_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supervisor_water_length = _parse_supervisor_water_length(d.pop("supervisorWaterLength", UNSET))

        def _parse_supervisor_wet_sides_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supervisor_wet_sides_length = _parse_supervisor_wet_sides_length(d.pop("supervisorWetSidesLength", UNSET))

        dipping_entry_actual_model = cls(
            crew_start_time=crew_start_time,
            crew_end_time=crew_end_time,
            crew_id=crew_id,
            crew_depth=crew_depth,
            crew_water_length=crew_water_length,
            crew_wet_sides_length=crew_wet_sides_length,
            crew_temperature=crew_temperature,
            crew_comment=crew_comment,
            supervisor_id=supervisor_id,
            supervisor_start_time=supervisor_start_time,
            supervisor_end_time=supervisor_end_time,
            supervisor_depth=supervisor_depth,
            supervisor_water_length=supervisor_water_length,
            supervisor_wet_sides_length=supervisor_wet_sides_length,
        )

        return dipping_entry_actual_model
