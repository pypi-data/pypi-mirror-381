# surak/policy.py
"""Policy schema and validation."""

from typing import Any, Dict, List, Optional, Union
from pathlib import Path
from datetime import datetime

import yaml
from pydantic import BaseModel, Field, field_validator, model_validator

from .exceptions import PolicyError, PolicyValidationError


class PolicyCondition(BaseModel):
    """A single condition in a policy."""
    
    resource: str = Field(..., description="Resource to check (e.g., 'branch', 'coverage')")
    operator: str = Field(..., description="Operator to use (e.g., 'equals', 'gte')")
    value: Any = Field(..., description="Expected value")
    name: Optional[str] = Field(None, description="Name for resource lookup (e.g., check suite name)")
    severity: str = Field("error", description="Severity level: 'error' or 'warning'")
    message: Optional[str] = Field(None, description="Custom message for violation")
    
    @field_validator("severity")
    @classmethod
    def validate_severity(cls, v: str) -> str:
        """Validate severity is one of allowed values."""
        if v not in ["error", "warning"]:
            raise PolicyValidationError(f"Severity must be 'error' or 'warning', got: {v}")
        return v
    
    def get_message(self, actual_value: Any = None) -> str:
        """Get violation message."""
        if self.message:
            return self.message
        
        # Generate default message
        if actual_value is not None:
            return (
                f"Resource '{self.resource}' failed: "
                f"expected {self.operator} {self.value}, got {actual_value}"
            )
        return f"Resource '{self.resource}' failed: expected {self.operator} {self.value}"


class PolicyTrigger(BaseModel):
    """Defines when a policy should be evaluated."""
    
    event: str = Field(..., description="Event type (e.g., 'deployment', 'pull_request')")
    environment: Optional[str] = Field(None, description="Target environment (e.g., 'production')")
    branches: Optional[List[str]] = Field(None, description="Branch filters")
    
    def matches(self, event_data: Dict[str, Any]) -> bool:
        """Check if this trigger matches the event data."""
        # Check event type
        if event_data.get("event") != self.event:
            return False
        
        # Check environment if specified
        if self.environment and event_data.get("environment") != self.environment:
            return False
        
        # Check branches if specified
        if self.branches:
            event_branch = event_data.get("branch", "")
            if not any(self._branch_matches(event_branch, pattern) for pattern in self.branches):
                return False
        
        return True
    
    @staticmethod
    def _branch_matches(branch: str, pattern: str) -> bool:
        """Check if branch matches pattern (supports wildcards)."""
        if pattern == "*":
            return True
        if "*" in pattern:
            import re
            regex_pattern = pattern.replace("*", ".*")
            return bool(re.match(f"^{regex_pattern}$", branch))
        return branch == pattern


class PolicyAction(BaseModel):
    """Action to take when policy passes or fails."""
    
    create_check: Optional[str] = Field(None, description="Create check status: 'pass' or 'fail'")
    block_deployment: bool = Field(False, description="Block deployment on failure")
    notify: Optional[List[str]] = Field(None, description="Notification targets")
    
    model_config = {"extra": "allow"}  # Allow additional fields for custom actions


class PolicyActions(BaseModel):
    """Actions for different policy outcomes."""
    
    on_pass: List[PolicyAction] = Field(default_factory=list, description="Actions when policy passes")
    on_fail: List[PolicyAction] = Field(default_factory=list, description="Actions when policy fails")


class PolicyMetadata(BaseModel):
    """Metadata about the policy."""
    
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    author: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    
    model_config = {"extra": "allow"}


class Policy(BaseModel):
    """A complete policy definition."""
    
    id: str = Field(..., description="Unique policy identifier")
    name: str = Field(..., description="Human-readable policy name")
    version: str = Field(default="1.0.0", description="Policy version")
    description: Optional[str] = Field(None, description="Policy description")
    
    enabled: bool = Field(default=True, description="Whether policy is enabled")
    
    triggers: List[PolicyTrigger] = Field(
        default_factory=list,
        description="When to evaluate this policy"
    )
    
    conditions: List[PolicyCondition] = Field(
        ...,
        description="Conditions that must be met"
    )
    
    actions: Optional[PolicyActions] = Field(
        None,
        description="Actions to take based on policy result"
    )
    
    metadata: Optional[PolicyMetadata] = Field(
        default_factory=PolicyMetadata,
        description="Additional metadata"
    )
    
    @field_validator("id")
    @classmethod
    def validate_id(cls, v: str) -> str:
        """Validate policy ID format."""
        if not v or not v.strip():
            raise PolicyValidationError("Policy ID cannot be empty")
        # Allow alphanumeric, hyphens, underscores, slashes (for namespacing)
        import re
        if not re.match(r'^[a-zA-Z0-9/_-]+$', v):
            raise PolicyValidationError(
                f"Policy ID must contain only alphanumeric characters, hyphens, underscores, or slashes: {v}"
            )
        return v
    
    @field_validator("version")
    @classmethod
    def validate_version(cls, v: str) -> str:
        """Validate version format (semver-ish)."""
        import re
        if not re.match(r'^\d+\.\d+\.\d+', v):
            raise PolicyValidationError(f"Version must be in format X.Y.Z: {v}")
        return v
    
    @model_validator(mode="after")
    def validate_policy(self) -> "Policy":
        """Validate the complete policy."""
        if not self.conditions:
            raise PolicyValidationError("Policy must have at least one condition")
        return self
    
    @classmethod
    def from_yaml(cls, yaml_str: str) -> "Policy":
        """Create policy from YAML string."""
        try:
            data = yaml.safe_load(yaml_str)
        except yaml.YAMLError as e:
            raise PolicyError(f"Invalid YAML: {e}") from e
        
        # Handle nested 'policy' key if present
        if "policy" in data:
            data = data["policy"]
        
        try:
            return cls(**data)
        except Exception as e:
            raise PolicyValidationError(f"Invalid policy structure: {e}") from e
    
    @classmethod
    def from_file(cls, filepath: Union[str, Path]) -> "Policy":
        """Load policy from YAML file."""
        path = Path(filepath)
        
        if not path.exists():
            raise PolicyError(f"Policy file not found: {filepath}")
        
        try:
            content = path.read_text()
            return cls.from_yaml(content)
        except Exception as e:
            raise PolicyError(f"Failed to load policy from {filepath}: {e}") from e
    
    def to_yaml(self) -> str:
        """Export policy to YAML string."""
        data = self.model_dump(exclude_none=True)
        return yaml.dump({"policy": data}, default_flow_style=False, sort_keys=False)
    
    def to_file(self, filepath: Union[str, Path]) -> None:
        """Save policy to YAML file."""
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_yaml())
    
    def should_evaluate(self, event_data: Dict[str, Any]) -> bool:
        """Check if this policy should be evaluated for the given event."""
        if not self.enabled:
            return False
        
        # If no triggers defined, evaluate for all events
        if not self.triggers:
            return True
        
        # Check if any trigger matches
        return any(trigger.matches(event_data) for trigger in self.triggers)
    
    def get_error_conditions(self) -> List[PolicyCondition]:
        """Get conditions with 'error' severity."""
        return [c for c in self.conditions if c.severity == "error"]
    
    def get_warning_conditions(self) -> List[PolicyCondition]:
        """Get conditions with 'warning' severity."""
        return [c for c in self.conditions if c.severity == "warning"]


class PolicyResult(BaseModel):
    """Result of policy evaluation."""
    
    policy_id: str
    policy_name: str
    policy_version: str
    
    passed: bool
    evaluated_at: datetime = Field(default_factory=datetime.now(datetime.timezone.utc))
    
    violations: List[str] = Field(default_factory=list, description="Error-level violations")
    warnings: List[str] = Field(default_factory=list, description="Warning-level violations")
    
    context: Dict[str, Any] = Field(default_factory=dict, description="Evaluation context")
    
    @property
    def has_violations(self) -> bool:
        """Check if there are any violations."""
        return len(self.violations) > 0
    
    @property
    def has_warnings(self) -> bool:
        """Check if there are any warnings."""
        return len(self.warnings) > 0
    
    def summary(self) -> str:
        """Get a summary of the result."""
        status = "✓ PASSED" if self.passed else "✗ FAILED"
        parts = [f"{status}: {self.policy_name}"]
        
        if self.violations:
            parts.append(f"{len(self.violations)} violation(s)")
        if self.warnings:
            parts.append(f"{len(self.warnings)} warning(s)")
        
        return " | ".join(parts)