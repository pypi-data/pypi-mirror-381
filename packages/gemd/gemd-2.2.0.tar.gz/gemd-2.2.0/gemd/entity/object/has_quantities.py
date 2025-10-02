"""For entities that hve quantities."""
from sys import float_info

from gemd.entity.bounds.real_bounds import RealBounds
from gemd.entity.value.continuous_value import ContinuousValue
from gemd.entity.value.base_value import BaseValue
from gemd.entity.bounds_validation import get_validation_level, WarningLevel
from gemd.entity.dict_serializable import logger

__all__ = ["HasQuantities"]


class HasQuantities(object):
    """Mixin-trait that includes the mass, volume, number fraction, and absolute quantity."""

    def __init__(self, *,
                 mass_fraction: ContinuousValue = None,
                 volume_fraction: ContinuousValue = None,
                 number_fraction: ContinuousValue = None,
                 absolute_quantity: ContinuousValue = None):

        self._mass_fraction = None
        self.mass_fraction = mass_fraction

        self._volume_fraction = None
        self.volume_fraction = volume_fraction

        self._number_fraction = None
        self.number_fraction = number_fraction

        self._absolute_quantity = None
        self.absolute_quantity = absolute_quantity

    @staticmethod
    def _check(value: BaseValue):
        fraction_bounds = RealBounds(lower_bound=0.0, upper_bound=1.0, default_units='')
        level = get_validation_level()
        accept = level == WarningLevel.IGNORE or fraction_bounds.contains(value)
        if not accept:
            message = f"Value {value} is not a dimensionless value between 0 and 1."
            if level == WarningLevel.WARNING:
                logger.warning(message)
            else:
                raise ValueError(message)

    @property
    def mass_fraction(self) -> ContinuousValue:
        """The mass fraction of the material."""
        return self._mass_fraction

    @mass_fraction.setter
    def mass_fraction(self, mass_fraction: ContinuousValue):
        if mass_fraction is None:
            self._mass_fraction = None
        elif not isinstance(mass_fraction, ContinuousValue):
            raise TypeError("mass_fraction was not given as a continuous value")
        else:
            self._check(mass_fraction)
            self._mass_fraction = mass_fraction

    @property
    def volume_fraction(self) -> ContinuousValue:
        """The volume fraction of the material."""
        return self._volume_fraction

    @volume_fraction.setter
    def volume_fraction(self, volume_fraction: ContinuousValue):
        if volume_fraction is None:
            self._volume_fraction = None
        elif not isinstance(volume_fraction, ContinuousValue):
            raise TypeError("volume_fraction was not given as a continuous value")
        else:
            self._check(volume_fraction)
            self._volume_fraction = volume_fraction

    @property
    def number_fraction(self) -> ContinuousValue:
        """The number fraction (commonly called mole fraction) of the material."""
        return self._number_fraction

    @number_fraction.setter
    def number_fraction(self, number_fraction: ContinuousValue):
        if number_fraction is None:
            self._number_fraction = None
        elif not isinstance(number_fraction, ContinuousValue):
            raise TypeError("number_fraction was not given as a continuous value")
        else:
            self._check(number_fraction)
            self._number_fraction = number_fraction

    @property
    def absolute_quantity(self) -> ContinuousValue:
        """The absolute quantity of the material."""
        return self._absolute_quantity

    @absolute_quantity.setter
    def absolute_quantity(self, absolute_quantity: ContinuousValue):
        if absolute_quantity is None:
            self._absolute_quantity = None
        elif not isinstance(absolute_quantity, ContinuousValue):
            raise TypeError("absolute_quantity was not given as a continuous value")
        else:
            max_bounds = RealBounds(
                lower_bound=0.0,
                upper_bound=float_info.max,
                default_units=absolute_quantity.units
            )
            dimensionless = RealBounds(
                lower_bound=0.0,
                upper_bound=float_info.max,
                default_units=''
            )
            level = get_validation_level()
            if level != WarningLevel.IGNORE:
                messages = []
                if not max_bounds.contains(absolute_quantity):
                    messages.append(f"Value {absolute_quantity} is less than 0.0.")
                if dimensionless.contains(absolute_quantity):
                    messages.append(f"Value {absolute_quantity} is dimensionless.")
                if level == WarningLevel.WARNING:
                    for message in messages:
                        logger.warning(message)
                else:
                    raise ValueError("; ".join(messages))
            self._absolute_quantity = absolute_quantity
