"""Discrete distribution across several categories."""
from typing import Optional, Union, Mapping

from gemd.entity.setters import validate_str
from gemd.entity.value.categorical_value import CategoricalValue
from gemd.entity.bounds import CategoricalBounds

__all__ = ["DiscreteCategorical"]


class DiscreteCategorical(CategoricalValue, typ="discrete_categorical"):
    """
    Distribution over a discrete set of categories.

    Parameters
    ----------
    probabilities: str or Map[str, float]
        The categories and their probabilities.

        If a string is provided, that string corresponds to the only category and is given a
        probability of 1.0

        If a dictionary is provided, then each key is a category and its value is the probability
        of that category. The probabilities *must* sum to 1.0.

    """

    def __init__(self, probabilities: Union[str, Mapping[str, float]] = None):
        self._probabilities = None
        self.probabilities = probabilities

    @property
    def probabilities(self) -> Mapping[str, float]:
        """Get the map from categories to probabilities."""
        return self._probabilities

    @probabilities.setter
    def probabilities(self, probabilities: Optional[Union[str, Mapping[str, float]]]):
        """Set the map from categories to probabilities."""
        if probabilities is None:
            self._probabilities = None
        elif isinstance(probabilities, str):
            self._probabilities = {validate_str(probabilities): 1.0}
        elif isinstance(probabilities, dict):
            if abs(sum(probabilities.values()) - 1.0) > 1.0e-9:
                raise ValueError("probabilities must sum to 1.0")
            self._probabilities = {validate_str(k): v for k, v in probabilities.items()}
        else:
            raise TypeError("probabilities must be dict or single value")

    def _to_bounds(self) -> CategoricalBounds:
        """
        Return the smallest bounds object that is consistent with the Value.

        Returns
        -------
        BaseBounds
            The minimally consistent
            :class:`~gemd.entity.bounds.categorical_bounds.CategoricalBounds`.

        """
        return CategoricalBounds(categories=set(self.probabilities))
