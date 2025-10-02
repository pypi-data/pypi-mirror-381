from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_plan_deck_model import ChargePlanDeckModel


T = TypeVar("T", bound="ChargePlanModel")


@_attrs_define
class ChargePlanModel:
    """The current plan of how a hole should be charged.

    Attributes:
        hole_id (Union[Unset, int]): The ID of the hole this charge plan relates to.
        decks (Union[List['ChargePlanDeckModel'], None, Unset]): The decks planned to be loaded into the hole.
    """

    hole_id: Union[Unset, int] = UNSET
    decks: Union[List["ChargePlanDeckModel"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        hole_id = self.hole_id

        decks: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.decks, Unset):
            decks = UNSET
        elif isinstance(self.decks, list):
            decks = []
            for decks_type_0_item_data in self.decks:
                decks_type_0_item = decks_type_0_item_data.to_dict()
                decks.append(decks_type_0_item)

        else:
            decks = self.decks

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if hole_id is not UNSET:
            field_dict["holeId"] = hole_id
        if decks is not UNSET:
            field_dict["decks"] = decks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.charge_plan_deck_model import ChargePlanDeckModel

        d = src_dict.copy()
        hole_id = d.pop("holeId", UNSET)

        def _parse_decks(data: object) -> Union[List["ChargePlanDeckModel"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                decks_type_0 = []
                _decks_type_0 = data
                for decks_type_0_item_data in _decks_type_0:
                    decks_type_0_item = ChargePlanDeckModel.from_dict(decks_type_0_item_data)

                    decks_type_0.append(decks_type_0_item)

                return decks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ChargePlanDeckModel"], None, Unset], data)

        decks = _parse_decks(d.pop("decks", UNSET))

        charge_plan_model = cls(
            hole_id=hole_id,
            decks=decks,
        )

        return charge_plan_model
