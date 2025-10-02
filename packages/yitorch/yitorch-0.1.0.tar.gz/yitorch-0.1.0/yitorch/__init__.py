# -*- coding: utf-8 -*-
"""导出公共接口"""

import importlib
import typing
from yitorch.const import __VERSION__

__version__ = __VERSION__

__all__ = [
    "cli",
    "const",
    "enums",
    "exceptions",
    "log",
]


# Copied from https://peps.python.org/pep-0562/
def __getattr__(name: str) -> typing.Any:
    if name in __all__:
        return importlib.import_module("." + name, __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
