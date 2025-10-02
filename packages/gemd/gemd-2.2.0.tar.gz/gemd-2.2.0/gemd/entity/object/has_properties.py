"""For entities that have properties."""
from gemd.entity.base_entity import BaseEntity
from gemd.entity.has_dependencies import HasDependencies
from gemd.entity.link_by_uid import LinkByUID
from gemd.entity.object.has_template_check_generator import HasTemplateCheckGenerator
from gemd.entity.template.has_property_templates import HasPropertyTemplates
from gemd.entity.attribute.property import Property
from gemd.entity.setters import validate_list

from typing import Union, Iterable, List, Set
from abc import ABC

__all__ = ["HasProperties"]


class HasProperties(HasTemplateCheckGenerator, HasDependencies, ABC):
    """Mixin-trait for entities that include properties."""

    def __init__(self, properties: Union[Property, Iterable[Property]]):
        self._properties = None
        self.properties = properties

    @property
    def properties(self) -> List[Property]:
        """A list of properties associated with this entity."""
        return self._properties

    @properties.setter
    def properties(self, properties: Union[Property, Iterable[Property]]):
        """Set the list of properties."""
        checker = self._generate_template_check(HasPropertyTemplates.validate_property)
        self._properties = validate_list(properties, Property, trigger=checker)

    def _local_dependencies(self) -> Set[Union[BaseEntity, LinkByUID]]:
        """Return a set of all immediate dependencies (no recursion)."""
        return {prop.template for prop in self.properties if prop.template is not None}
