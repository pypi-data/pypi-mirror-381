from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorModel")


@_attrs_define
class ErrorModel:
    """A structure of error messages given when a request could not be fulfilled.

    Attributes:
        title (Union[None, Unset, str]):
        details (Union[None, Unset, str]):
        errors (Union[List[str], None, Unset]):
    """

    title: Union[None, Unset, str] = UNSET
    details: Union[None, Unset, str] = UNSET
    errors: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        details: Union[None, Unset, str]
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        errors: Union[List[str], None, Unset]
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if details is not UNSET:
            field_dict["details"] = details
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_details(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_errors(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(List[str], data)

                return errors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        errors = _parse_errors(d.pop("errors", UNSET))

        error_model = cls(
            title=title,
            details=details,
            errors=errors,
        )

        return error_model
