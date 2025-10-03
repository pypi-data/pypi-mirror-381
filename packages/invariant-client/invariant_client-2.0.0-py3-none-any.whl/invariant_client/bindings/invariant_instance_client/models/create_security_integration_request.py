from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.oidc_security_integration_metadata import (
        OIDCSecurityIntegrationMetadata,
    )


T = TypeVar("T", bound="CreateSecurityIntegrationRequest")


@_attrs_define
class CreateSecurityIntegrationRequest:
    """
    Attributes:
        metadata (OIDCSecurityIntegrationMetadata):
    """

    metadata: "OIDCSecurityIntegrationMetadata"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oidc_security_integration_metadata import (
            OIDCSecurityIntegrationMetadata,
        )

        d = dict(src_dict)
        metadata = OIDCSecurityIntegrationMetadata.from_dict(d.pop("metadata"))

        create_security_integration_request = cls(
            metadata=metadata,
        )

        create_security_integration_request.additional_properties = d
        return create_security_integration_request

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
