# surak/operators.py
"""Operators for policy condition evaluation."""

from typing import Any, Callable, Dict
from datetime import datetime, time
import re

from .exceptions import OperatorError


class Operator:
    """Base class for operators."""
    
    def __init__(self, name: str, func: Callable[[Any, Any], bool], description: str = ""):
        self.name = name
        self.func = func
        self.description = description
    
    def evaluate(self, actual: Any, expected: Any) -> bool:
        """Evaluate the operator."""
        try:
            return self.func(actual, expected)
        except Exception as e:
            raise OperatorError(f"Operator '{self.name}' failed: {e}") from e


# Standard comparison operators
def _equals(actual: Any, expected: Any) -> bool:
    """Check if actual equals expected."""
    return actual == expected


def _not_equals(actual: Any, expected: Any) -> bool:
    """Check if actual does not equal expected."""
    return actual != expected


def _greater_than(actual: Any, expected: Any) -> bool:
    """Check if actual is greater than expected."""
    return actual > expected


def _greater_than_or_equal(actual: Any, expected: Any) -> bool:
    """Check if actual is greater than or equal to expected."""
    return actual >= expected


def _less_than(actual: Any, expected: Any) -> bool:
    """Check if actual is less than expected."""
    return actual < expected


def _less_than_or_equal(actual: Any, expected: Any) -> bool:
    """Check if actual is less than or equal to expected."""
    return actual <= expected


# String operators
def _contains(actual: Any, expected: Any) -> bool:
    """Check if actual contains expected."""
    if isinstance(actual, str):
        return expected in actual
    elif isinstance(actual, (list, tuple)):
        return expected in actual
    return False


def _starts_with(actual: str, expected: str) -> bool:
    """Check if actual starts with expected."""
    return str(actual).startswith(expected)


def _ends_with(actual: str, expected: str) -> bool:
    """Check if actual ends with expected."""
    return str(actual).endswith(expected)


def _matches(actual: str, pattern: str) -> bool:
    """Check if actual matches regex pattern."""
    return bool(re.match(pattern, str(actual)))


# List/Collection operators
def _in(actual: Any, expected: list) -> bool:
    """Check if actual is in expected list."""
    return actual in expected


def _not_in(actual: Any, expected: list) -> bool:
    """Check if actual is not in expected list."""
    return actual not in expected


# Special operators
def _status_equals(actual: Dict[str, Any], expected: str) -> bool:
    """Check if status in actual dict equals expected."""
    if not isinstance(actual, dict):
        return False
    return actual.get("status") == expected


def _has_approval_from(approvals: list, teams: list) -> bool:
    """Check if all required teams have approved."""
    if not isinstance(approvals, list):
        return False
    
    approved_teams = {
        approval.get("team") 
        for approval in approvals 
        if approval.get("approved")
    }
    
    return all(team in approved_teams for team in teams)


def _within_window(current_time: datetime, window: Dict[str, Any]) -> bool:
    """Check if current time is within specified window."""
    start = time.fromisoformat(window.get("start", "00:00"))
    end = time.fromisoformat(window.get("end", "23:59"))
    
    current = current_time.time()
    
    if start <= end:
        return start <= current <= end
    else:
        # Handle overnight window (e.g., 22:00 to 02:00)
        return current >= start or current <= end


# Registry of all operators
OPERATORS: Dict[str, Operator] = {
    "equals": Operator("equals", _equals, "Check equality"),
    "not_equals": Operator("not_equals", _not_equals, "Check inequality"),
    "gt": Operator("gt", _greater_than, "Greater than"),
    "gte": Operator("gte", _greater_than_or_equal, "Greater than or equal"),
    "lt": Operator("lt", _less_than, "Less than"),
    "lte": Operator("lte", _less_than_or_equal, "Less than or equal"),
    "contains": Operator("contains", _contains, "Contains value"),
    "starts_with": Operator("starts_with", _starts_with, "Starts with"),
    "ends_with": Operator("ends_with", _ends_with, "Ends with"),
    "matches": Operator("matches", _matches, "Matches regex pattern"),
    "in": Operator("in", _in, "In list"),
    "not_in": Operator("not_in", _not_in, "Not in list"),
    "status_equals": Operator("status_equals", _status_equals, "Status equals"),
    "has_approval_from": Operator("has_approval_from", _has_approval_from, "Has approval from teams"),
    "within_window": Operator("within_window", _within_window, "Within time window"),
}


def get_operator(name: str) -> Operator:
    """Get an operator by name."""
    operator = OPERATORS.get(name)
    if not operator:
        raise OperatorError(f"Unknown operator: {name}")
    return operator


def register_operator(name: str, func: Callable[[Any, Any], bool], description: str = "") -> None:
    """Register a custom operator."""
    OPERATORS[name] = Operator(name, func, description)


def list_operators() -> Dict[str, str]:
    """List all available operators with descriptions."""
    return {name: op.description for name, op in OPERATORS.items()}