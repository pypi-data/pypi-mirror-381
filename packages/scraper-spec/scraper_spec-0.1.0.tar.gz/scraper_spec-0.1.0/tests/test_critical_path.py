"""Tests for critical path validation."""
import os
import tempfile
import pytest
from framework.utils import (
    load_critical_path_config,
    validate_critical_path_in_plan,
    ensure_critical_path_in_plan
)


def test_load_default_critical_path_when_no_config():
    """Test loading default phases when config doesn't exist."""
    phases = load_critical_path_config("/nonexistent/path/config.yaml")
    assert phases == ["Acquire", "Identify", "Collect", "Extract"]


def test_load_custom_critical_path_from_config():
    """Test loading custom phases from config file."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""critical_path:
  phases:
    - Connect
    - Discover
    - Retrieve
    - Transform
    - Validate
""")
        config_path = f.name
    
    try:
        phases = load_critical_path_config(config_path)
        assert phases == ["Connect", "Discover", "Retrieve", "Transform", "Validate"]
    finally:
        os.unlink(config_path)


def test_validate_plan_with_all_phases_in_order():
    """Test validation passes when all phases appear in correct order."""
    plan_content = """
# Implementation Plan

## Phase 1: Acquire
Connect to the data source.

## Phase 2: Identify
Locate target elements.

## Phase 3: Collect
Gather raw data.

## Phase 4: Extract
Transform to structured output.
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""critical_path:
  phases:
    - Acquire
    - Identify
    - Collect
    - Extract
""")
        config_path = f.name
    
    try:
        is_valid, error = validate_critical_path_in_plan(plan_content, config_path)
        assert is_valid is True
        assert error is None
    finally:
        os.unlink(config_path)


def test_validate_plan_missing_phase():
    """Test validation fails when a phase is missing."""
    plan_content = """
# Implementation Plan

## Phase 1: Acquire
Connect to the data source.

## Phase 2: Identify
Locate target elements.

## Phase 4: Extract
Transform to structured output.
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""critical_path:
  phases:
    - Acquire
    - Identify
    - Collect
    - Extract
""")
        config_path = f.name
    
    try:
        is_valid, error = validate_critical_path_in_plan(plan_content, config_path)
        assert is_valid is False
        assert "Collect" in error
        assert "missing" in error
    finally:
        os.unlink(config_path)


def test_validate_plan_phases_out_of_order():
    """Test validation fails when phases appear in wrong order."""
    plan_content = """
# Implementation Plan

## Phase 1: Acquire
Connect to the data source.

## Phase 2: Collect
Gather raw data.

## Phase 3: Identify
Locate target elements.

## Phase 4: Extract
Transform to structured output.
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""critical_path:
  phases:
    - Acquire
    - Identify
    - Collect
    - Extract
""")
        config_path = f.name
    
    try:
        is_valid, error = validate_critical_path_in_plan(plan_content, config_path)
        assert is_valid is False
        assert "appears before" in error
        assert "Collect" in error or "Identify" in error
    finally:
        os.unlink(config_path)


def test_legacy_ensure_critical_path_function():
    """Test legacy function still works for backward compatibility."""
    plan_content = """
# Implementation Plan

## Acquire
Connect.

## Identify
Locate.

## Collect
Gather.

## Extract
Transform.
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""critical_path:
  phases:
    - Acquire
    - Identify
    - Collect
    - Extract
""")
        config_path = f.name
    
    try:
        # Legacy function should work but won't provide error details
        result = ensure_critical_path_in_plan(plan_content)
        assert result is True
    finally:
        os.unlink(config_path)


def test_case_insensitive_phase_matching():
    """Test that phase matching is case-insensitive."""
    plan_content = """
# Implementation Plan

## ACQUIRE
Connect.

## identify
Locate.

## CoLLeCt
Gather.

## extract
Transform.
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""critical_path:
  phases:
    - Acquire
    - Identify
    - Collect
    - Extract
""")
        config_path = f.name
    
    try:
        is_valid, error = validate_critical_path_in_plan(plan_content, config_path)
        assert is_valid is True
        assert error is None
    finally:
        os.unlink(config_path)


def test_empty_phases_list_passes_validation():
    """Test that empty phases list allows any plan."""
    plan_content = "Any content here"
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("""critical_path:
  phases: []
""")
        config_path = f.name
    
    try:
        is_valid, error = validate_critical_path_in_plan(plan_content, config_path)
        assert is_valid is True
        assert error is None
    finally:
        os.unlink(config_path)


def test_malformed_config_uses_defaults():
    """Test that malformed config falls back to defaults."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        f.write("malformed: yaml: content:")
        config_path = f.name
    
    try:
        phases = load_critical_path_config(config_path)
        assert phases == ["Acquire", "Identify", "Collect", "Extract"]
    finally:
        os.unlink(config_path)

