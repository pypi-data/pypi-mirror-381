from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.density_table_row import DensityTableRow


T = TypeVar("T", bound="ProductModel")


@_attrs_define
class ProductModel:
    """A consumable product used to blast holes.

    Attributes:
        product_id (Union[Unset, int]): The unique identifier of this product.
        name (Union[None, Unset, str]): The name of this product.
        description (Union[None, Unset, str]): The description of this product. Can be null
        integration_id (Union[None, Unset, str]): The identifier to help match this product in another system. Can be
            null.
        type (Union[None, Unset, str]): The type of this product.
        open_cup_density (Union[None, Unset, float]): The open cup density of this product (kg/m3). Can be null.
        energy_density (Union[None, Unset, float]): The energy released when this product is detonated (J/kg). Can be
            null.
        density_table (Union[List['DensityTableRow'], None, Unset]): The density of this product at specific depths. Can
            be null.
    """

    product_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    integration_id: Union[None, Unset, str] = UNSET
    type: Union[None, Unset, str] = UNSET
    open_cup_density: Union[None, Unset, float] = UNSET
    energy_density: Union[None, Unset, float] = UNSET
    density_table: Union[List["DensityTableRow"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        integration_id: Union[None, Unset, str]
        if isinstance(self.integration_id, Unset):
            integration_id = UNSET
        else:
            integration_id = self.integration_id

        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        open_cup_density: Union[None, Unset, float]
        if isinstance(self.open_cup_density, Unset):
            open_cup_density = UNSET
        else:
            open_cup_density = self.open_cup_density

        energy_density: Union[None, Unset, float]
        if isinstance(self.energy_density, Unset):
            energy_density = UNSET
        else:
            energy_density = self.energy_density

        density_table: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.density_table, Unset):
            density_table = UNSET
        elif isinstance(self.density_table, list):
            density_table = []
            for density_table_type_0_item_data in self.density_table:
                density_table_type_0_item = density_table_type_0_item_data.to_dict()
                density_table.append(density_table_type_0_item)

        else:
            density_table = self.density_table

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if integration_id is not UNSET:
            field_dict["integrationId"] = integration_id
        if type is not UNSET:
            field_dict["type"] = type
        if open_cup_density is not UNSET:
            field_dict["openCupDensity"] = open_cup_density
        if energy_density is not UNSET:
            field_dict["energyDensity"] = energy_density
        if density_table is not UNSET:
            field_dict["densityTable"] = density_table

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.density_table_row import DensityTableRow

        d = src_dict.copy()
        product_id = d.pop("productId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_integration_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        integration_id = _parse_integration_id(d.pop("integrationId", UNSET))

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("type", UNSET))

        def _parse_open_cup_density(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        open_cup_density = _parse_open_cup_density(d.pop("openCupDensity", UNSET))

        def _parse_energy_density(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        energy_density = _parse_energy_density(d.pop("energyDensity", UNSET))

        def _parse_density_table(data: object) -> Union[List["DensityTableRow"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                density_table_type_0 = []
                _density_table_type_0 = data
                for density_table_type_0_item_data in _density_table_type_0:
                    density_table_type_0_item = DensityTableRow.from_dict(density_table_type_0_item_data)

                    density_table_type_0.append(density_table_type_0_item)

                return density_table_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["DensityTableRow"], None, Unset], data)

        density_table = _parse_density_table(d.pop("densityTable", UNSET))

        product_model = cls(
            product_id=product_id,
            name=name,
            description=description,
            integration_id=integration_id,
            type=type,
            open_cup_density=open_cup_density,
            energy_density=energy_density,
            density_table=density_table,
        )

        return product_model
