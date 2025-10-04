# surak/exceptions.py
"""Custom exceptions for Surak policy engine."""


class SurakError(Exception):
    """Base exception for all Surak errors."""
    pass


class PolicyError(SurakError):
    """Raised when there's an issue with policy definition or validation."""
    pass


class PolicyValidationError(PolicyError):
    """Raised when policy validation fails."""
    pass


class PluginError(SurakError):
    """Raised when there's an issue with a plugin."""
    pass


class PluginNotFoundError(PluginError):
    """Raised when a requested plugin is not registered."""
    pass


class EvaluationError(SurakError):
    """Raised when policy evaluation fails."""
    pass


class OperatorError(SurakError):
    """Raised when an operator is invalid or fails."""
    pass


class ResourceError(SurakError):
    """Raised when a resource cannot be accessed or is invalid."""
    pass