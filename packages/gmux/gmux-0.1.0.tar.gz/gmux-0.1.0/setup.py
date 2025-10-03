from __future__ import annotations

from setuptools import setup
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(self):  # type: ignore[override]
        return True

    def is_pure(self):  # type: ignore[override]
        return False


setup(distclass=BinaryDistribution)
