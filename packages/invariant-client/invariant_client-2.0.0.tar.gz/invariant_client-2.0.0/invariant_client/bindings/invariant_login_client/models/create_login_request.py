from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateLoginRequest")


@_attrs_define
class CreateLoginRequest:
    """This request creates a new login from an invite link. It does not require any credential.

    Attributes:
        type_ (Literal['new_login']):
        email (str):
        password (str):
        ilink (str):
    """

    type_: Literal["new_login"]
    email: str
    password: str
    ilink: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        email = self.email

        password = self.password

        ilink = self.ilink

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "email": email,
                "password": password,
                "ilink": ilink,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["new_login"], d.pop("type"))
        if type_ != "new_login":
            raise ValueError(f"type must match const 'new_login', got '{type_}'")

        email = d.pop("email")

        password = d.pop("password")

        ilink = d.pop("ilink")

        create_login_request = cls(
            type_=type_,
            email=email,
            password=password,
            ilink=ilink,
        )

        create_login_request.additional_properties = d
        return create_login_request

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
