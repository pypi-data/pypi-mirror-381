from abc import ABC, ABCMeta
from logging import getLogger

import inspect
import functools
from typing import TypeVar, Union, Iterable, List, Mapping, Dict, Set, Any

__all__ = ["DictSerializable"]

# There are some weird (probably resolvable) errors during object cloning if this is an
# instance variable of DictSerializable.
logger = getLogger(__name__)

DictSerializableType = TypeVar("DictSerializableType", bound="DictSerializable")


class DictSerializableMeta(ABCMeta):
    """Metaclass for tracking DictSerializable type string to class mappings."""

    _class: Dict[str, type] = {}

    def __new__(mcs, name, bases, *args,  # noqa: D102
                typ: str = None, skip: Set[str] = frozenset(),
                **kwargs):
        return super().__new__(mcs, name, bases, *args, **kwargs)

    def __init__(cls, name, bases, *args, typ: str = None, skip: Set[str] = frozenset(), **kwargs):
        super().__init__(name, bases, *args, **kwargs)
        if typ is not None:
            if typ in cls._class and not issubclass(cls, cls._class.get(typ)):
                raise ValueError(f"{cls} attempted to take typ {typ} from {cls._class.get(typ)}, "
                                 f"which is not its ancestor.")
            cls.typ = typ
            cls._class[typ] = cls
        elif not hasattr(cls, "typ"):
            cls.typ = NotImplementedError
        cls.skip = {x for b in bases for x in getattr(b, 'skip', {})} | skip

    @property
    def class_mapping(cls) -> Dict[str, type]:
        """
        Return class typ string -> class map for DictSerializable and its descendants.

        Note that is actually returns a copy of the internal dict to avoid accidental breakage.

        Returns
        -------
        Dict[str, type]
            The mapping from typ string to class

        """
        return cls._class.copy()


class DictSerializable(ABC, metaclass=DictSerializableMeta):
    """A base class for objects that can be represented as a dictionary and serialized."""

    @classmethod
    def from_dict(cls, d: Mapping[str, Any]) -> DictSerializableType:
        """
        Reconstitute the object from a dictionary.

        Parameters
        ----------
        d: dict
            The object as a dictionary of key-value pairs that correspond to the object's fields.

        Returns
        -------
        DictSerializable
            The deserialized object.

        """
        expected_arg_names = cls._init_sig()
        kwargs = {}
        for name, arg in d.items():
            if name in expected_arg_names:
                kwargs[name] = arg
            elif name != 'type':
                logger.warning('Ignoring unexpected keyword argument in {}: {}'.format(
                    cls.__name__, name))
        # noinspection PyArgumentList
        # DictSerializable's constructor is not intended for use,
        # but all of its children will use from_dict like this.
        return cls(**kwargs)

    @classmethod
    @functools.lru_cache(maxsize=1024)
    def _init_sig(cls) -> List[str]:
        """Internal method for generating the argument names for the class init method."""
        expected_arg_names = inspect.getfullargspec(cls.__init__).args
        expected_arg_names += inspect.getfullargspec(cls.__init__).kwonlyargs
        return expected_arg_names

    def as_dict(self) -> Dict[str, Any]:
        """
        Convert the object to a dictionary.

        Returns
        -------
        dict
            A dictionary representation of the object, where the keys are its fields.

        """
        keys = {x.lstrip('_') for x in vars(self) if x not in self.skip}
        attributes = {k: self.__getattribute__(k) for k in keys}
        attributes["type"] = self.typ
        return attributes

    def dump(self) -> Dict[str, Any]:
        """
        Convert the object to a JSON dictionary, so that every entry is serialized.

        Uses the json encoder client, so objects with uids are converted to LinkByUID dictionaries.

        Returns
        -------
        str
            A string representation of the object as a dictionary.

        """
        from gemd.json import GEMDJson
        import json

        encoder = GEMDJson()
        return json.loads(encoder.raw_dumps(self))

    @staticmethod
    def build(d: Mapping[str, Any]) -> DictSerializableType:
        """
        Build an object from a JSON dictionary.

        This differs from `from_dict` in that the values themselves may *also* be dictionaries
        corresponding to serialized DictSerializable objects.

        Parameters
        ----------
        d: dict
            The object as a serialized dictionary.

        Returns
        -------
        DictSerializable
            The deserialized object.

        """
        from gemd.json import GEMDJson
        encoder = GEMDJson()
        return encoder.raw_loads(encoder.raw_dumps(d))

    def __repr__(self) -> str:
        object_dict = self.as_dict()
        # as_dict() skips over keys in `skip`, but they should be in the representation.
        skipped_keys = {x.lstrip('_') for x in self.skip}
        for key in skipped_keys:
            skipped_field = getattr(self, key, None)
            object_dict[key] = self._name_repr(skipped_field)
        return str(object_dict)

    def _name_repr(self,
                   entity: Union[Iterable[DictSerializableType], DictSerializableType]) -> str:
        """
        A representation of an object or a list of objects that uses the name and type.

        This is used to represent soft-linked objects without inundating the user with
        repetitive information.

        Parameters
        ----------
        entity: DictSerializable or List[DictSerializable]
            Object to represent using its name. Generally a (list of) BaseEntity or BaseAttribute,
            both of which have a `name` field.

        Returns
        -------
        str
            A representation of `entity` using its name.

        """
        if isinstance(entity, Iterable):
            return [self._name_repr(item) for item in entity]
        elif entity is None:
            return None
        else:
            name = getattr(entity, 'name', '<unknown name>')
            return f"<{type(entity).__name__} '{name}'>"

    def _dict_for_compare(self) -> Dict[str, Any]:
        """Which fields & values are relevant to an equality test."""
        return self.as_dict()

    def __eq__(self, other):
        if isinstance(other, DictSerializable):
            self_dict = self._dict_for_compare()
            other_dict = other._dict_for_compare()
            return self_dict == other_dict
        else:
            return NotImplemented

    # Note the hash function checks if objects are identical, as opposed to the equals method,
    # which checks if fields are equal.  This is because BaseEntities are fundamentally
    # mutable objects.  Note that if you define an __eq__ method without defining a __hash__
    # method, the object will become unhashable.
    # https://docs.python.org/3/reference/datamodel.html#object.__hash
    def __hash__(self):
        return super().__hash__()
