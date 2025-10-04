#!/usr/bin/env python3
"""Quick test of exceptions and operators."""

from surak.exceptions import OperatorError, PolicyError
from surak.operators import get_operator, list_operators

# Test exceptions
try:
    raise PolicyError("Test error")
except PolicyError as e:
    print(f"✓ Exception works: {e}")

# Test operators
print(f"\n✓ Available operators: {len(list_operators())}")

# Test a few operators
op_equals = get_operator("equals")
assert op_equals.evaluate(5, 5) == True
assert op_equals.evaluate(5, 10) == False
print("✓ equals operator works")

op_gte = get_operator("gte")
assert op_gte.evaluate(10, 5) == True
assert op_gte.evaluate(5, 10) == False
print("✓ gte operator works")

op_contains = get_operator("contains")
assert op_contains.evaluate("hello world", "world") == True
assert op_contains.evaluate([1, 2, 3], 2) == True
print("✓ contains operator works")

print("\n🎉 Basic components working!")
