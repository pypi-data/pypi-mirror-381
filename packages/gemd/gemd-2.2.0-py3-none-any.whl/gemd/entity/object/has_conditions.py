"""For entities that have conditions."""
from gemd.entity.base_entity import BaseEntity
from gemd.entity.has_dependencies import HasDependencies
from gemd.entity.link_by_uid import LinkByUID
from gemd.entity.object.has_template_check_generator import HasTemplateCheckGenerator
from gemd.entity.template.has_condition_templates import HasConditionTemplates
from gemd.entity.attribute.condition import Condition
from gemd.entity.setters import validate_list

from typing import Union, Iterable, List, Set
from abc import ABC

__all__ = ["HasConditions"]


class HasConditions(HasTemplateCheckGenerator, HasDependencies, ABC):
    """Mixin-trait for entities that include conditions."""

    def __init__(self, conditions: Union[Condition, Iterable[Condition]]):
        self._conditions = None
        self.conditions = conditions

    @property
    def conditions(self) -> List[Condition]:
        """A list of conditions associated with this entity."""
        return self._conditions

    @conditions.setter
    def conditions(self, conditions: Union[Condition, Iterable[Condition]]):
        """Set the list of conditions."""
        checker = self._generate_template_check(HasConditionTemplates.validate_condition)
        self._conditions = validate_list(conditions, Condition, trigger=checker)

    def _local_dependencies(self) -> Set[Union[BaseEntity, LinkByUID]]:
        """Return a set of all immediate dependencies (no recursion)."""
        return {cond.template for cond in self.conditions if cond.template is not None}
