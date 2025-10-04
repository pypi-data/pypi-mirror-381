import inspect
import unittest
from typing import *

from setsig import core


class Test0(unittest.TestCase):
    def test_0(self: Self) -> None:
        def f(x: int) -> float:
            "This function decimates."
            return x / 10

        @core.SetSig(f)
        def g(y, /):
            "This function halfs."
            return y / 2

        self.assertEqual(
            inspect.signature(f),
            inspect.signature(g),
        )
        self.assertNotEqual(
            f.__doc__,
            g.__doc__,
        )


if __name__ == "__main__":
    unittest.main()
