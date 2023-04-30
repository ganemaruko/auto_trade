"""Exceptions about Strategy class."""
from core.exception.base import AutoTradeError


class StrategyError(AutoTradeError):
    """The base class about Strategy class."""


class ValidationError(StrategyError):
    def __str__(self):
        return f"Validation error!"
