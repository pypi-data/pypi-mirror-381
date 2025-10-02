from gemd.entity.attribute.base_attribute import BaseAttribute
from gemd.entity.template import ParameterTemplate

from typing import Type

__all__ = ["Parameter"]


class Parameter(BaseAttribute, typ="parameter"):
    """
    Parameter of a process or measurement.

    Parameters are the non-environmental variables (typically specified and controlled) that may
    affect a process or measurement: e.g. oven dial temperature for a kiln firing, magnification
    for a measurement taken with an electron microscope.

    Parameters
    ----------
    name: str
        Required name of the attribute. Each attribute within an object must have a unique name.
    notes: str
        Optional free-form notes about the attribute.
    value: ~gemd.entity.value.base_value.BaseValue
        The value of the attribute.
    template: ~gemd.entity.template.attribute_template.AttributeTemplate
        Attribute template that defines the allowed bounds of this attribute. If a template
        and value are both present then the value must be within the template bounds.
    origin: str
        The origin of the attribute. Must be one of "measured", "predicted", "summary",
        "specified", "computed", or "unknown." Default is "unknown."
    file_links: List[~gemd.entity.file_link.FileLink]
        Links to files associated with the attribute.

    """

    @staticmethod
    def _template_type() -> Type:
        return ParameterTemplate
