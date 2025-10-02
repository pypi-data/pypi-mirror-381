from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackfillingEntryPlan")


@_attrs_define
class BackfillingEntryPlan:
    """Instructions on how a backfilling activity should be performed.

    Attributes:
        target_depth (Union[None, Unset, float]): The desired depth of the hole after backfilling (Meters). Cannot be
            negative.
        crew_check_required (Union[Unset, bool]): Whether or not the hole requires re-dipping after backfilling by the
            crew.
        supervisor_check_required (Union[Unset, bool]): Whether or not the hole requires re-dipping after backfilling by
            the supervisor.
    """

    target_depth: Union[None, Unset, float] = UNSET
    crew_check_required: Union[Unset, bool] = UNSET
    supervisor_check_required: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        target_depth: Union[None, Unset, float]
        if isinstance(self.target_depth, Unset):
            target_depth = UNSET
        else:
            target_depth = self.target_depth

        crew_check_required = self.crew_check_required

        supervisor_check_required = self.supervisor_check_required

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if target_depth is not UNSET:
            field_dict["targetDepth"] = target_depth
        if crew_check_required is not UNSET:
            field_dict["crewCheckRequired"] = crew_check_required
        if supervisor_check_required is not UNSET:
            field_dict["supervisorCheckRequired"] = supervisor_check_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_target_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        target_depth = _parse_target_depth(d.pop("targetDepth", UNSET))

        crew_check_required = d.pop("crewCheckRequired", UNSET)

        supervisor_check_required = d.pop("supervisorCheckRequired", UNSET)

        backfilling_entry_plan = cls(
            target_depth=target_depth,
            crew_check_required=crew_check_required,
            supervisor_check_required=supervisor_check_required,
        )

        return backfilling_entry_plan
