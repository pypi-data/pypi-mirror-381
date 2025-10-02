from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargePlanDeckModel")


@_attrs_define
class ChargePlanDeckModel:
    """Details of how a deck is planned to be loaded.

    Attributes:
        product_id (Union[Unset, int]): The ID of the product to use in this deck.
        order (Union[Unset, int]): The order this deck sits in this hole. Decks are numbered from the bottom up, with
            the bottom deck having order '1'.
        length (Union[Unset, float]): The length of this deck measured along the length of the hole (Meters).
        mass (Union[None, Unset, float]): For products where the mass is known, the total mass of the deck (Kilograms).
        quantity (Union[None, Unset, float]): For packaged products, the number of packages or units used in this deck.
    """

    product_id: Union[Unset, int] = UNSET
    order: Union[Unset, int] = UNSET
    length: Union[Unset, float] = UNSET
    mass: Union[None, Unset, float] = UNSET
    quantity: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        order = self.order

        length = self.length

        mass: Union[None, Unset, float]
        if isinstance(self.mass, Unset):
            mass = UNSET
        else:
            mass = self.mass

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if order is not UNSET:
            field_dict["order"] = order
        if length is not UNSET:
            field_dict["length"] = length
        if mass is not UNSET:
            field_dict["mass"] = mass
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("productId", UNSET)

        order = d.pop("order", UNSET)

        length = d.pop("length", UNSET)

        def _parse_mass(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        mass = _parse_mass(d.pop("mass", UNSET))

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        charge_plan_deck_model = cls(
            product_id=product_id,
            order=order,
            length=length,
            mass=mass,
            quantity=quantity,
        )

        return charge_plan_deck_model
