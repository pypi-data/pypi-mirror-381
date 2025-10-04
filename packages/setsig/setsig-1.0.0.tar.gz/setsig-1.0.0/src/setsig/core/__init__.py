import inspect
from typing import *

import setdoc

__all__ = ["SetSig"]


class SetSig:

    @setdoc.basic
    def __call__(self: Self, target: Any) -> Any:
        target.__signature__ = self.value
        return target

    @setdoc.basic
    def __init__(self: Self, callable: Callable) -> None:
        self.value = inspect.signature(callable)
