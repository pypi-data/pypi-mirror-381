from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PasswordResetPINChallenge")


@_attrs_define
class PasswordResetPINChallenge:
    """The user must prove control of the email address by PIN before proceeding to reset the password.

    Attributes:
        type_ (Literal['reset_pin']):
    """

    type_: Literal["reset_pin"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["reset_pin"], d.pop("type"))
        if type_ != "reset_pin":
            raise ValueError(f"type must match const 'reset_pin', got '{type_}'")

        password_reset_pin_challenge = cls(
            type_=type_,
        )

        password_reset_pin_challenge.additional_properties = d
        return password_reset_pin_challenge

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
