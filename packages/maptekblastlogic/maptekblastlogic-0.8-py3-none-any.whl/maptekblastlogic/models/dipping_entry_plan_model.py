from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DippingEntryPlanModel")


@_attrs_define
class DippingEntryPlanModel:
    """Instructions on how to dip the holes.

    Attributes:
        last_known_depth (Union[None, Unset, float]): The last known depth of the hole when this entry was created
            (Meters). Can be null if unknown.
        supervisor_check_required (Union[Unset, bool]): Whether the supervisor is required to validate the dip
            measurements.
    """

    last_known_depth: Union[None, Unset, float] = UNSET
    supervisor_check_required: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        last_known_depth: Union[None, Unset, float]
        if isinstance(self.last_known_depth, Unset):
            last_known_depth = UNSET
        else:
            last_known_depth = self.last_known_depth

        supervisor_check_required = self.supervisor_check_required

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if last_known_depth is not UNSET:
            field_dict["lastKnownDepth"] = last_known_depth
        if supervisor_check_required is not UNSET:
            field_dict["supervisorCheckRequired"] = supervisor_check_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_last_known_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_known_depth = _parse_last_known_depth(d.pop("lastKnownDepth", UNSET))

        supervisor_check_required = d.pop("supervisorCheckRequired", UNSET)

        dipping_entry_plan_model = cls(
            last_known_depth=last_known_depth,
            supervisor_check_required=supervisor_check_required,
        )

        return dipping_entry_plan_model
