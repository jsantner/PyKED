from pint import UnitRegistry, set_application_registry
units = UnitRegistry()
"""Unit registry to contain the units used in PyKED"""
units.define('cm3 = centimeter**3')
Q_ = units.Quantity
set_application_registry(units)

from .chemked import ChemKED  # noqa: F401
from ._version import __version__  # noqa: F401
