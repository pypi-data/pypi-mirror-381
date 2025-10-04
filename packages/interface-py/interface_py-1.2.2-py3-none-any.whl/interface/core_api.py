from .core import InterfaceMeta as _InterfaceMeta


class _InterfaceBase(metaclass=_InterfaceMeta):
    """Hidden base class for all interfaces (not exposed to the user)."""
    pass


def _mark_interface(cls):
    cls._is_interface_ = True
    cls.__validate__()
    return cls


def interface(cls):
    if _InterfaceBase not in cls.__mro__:
        cls = type(cls.__name__, (_InterfaceBase,) + cls.__bases__, dict(cls.__dict__))

    return _mark_interface(cls)


def concrete(cls):
    cls._is_interface_ = False
    cls.__validate__()
    return cls
