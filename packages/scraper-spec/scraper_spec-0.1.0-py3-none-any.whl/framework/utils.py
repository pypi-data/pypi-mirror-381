"""
Utility functions for the scraper specification framework.
"""
import json
import yaml
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
import difflib


def get_iso8601_timestamp() -> str:
    """Generate ISO8601 timestamp."""
    return datetime.utcnow().isoformat() + 'Z'


def write_json_safely(filepath: str, data: Dict[str, Any]) -> bool:
    """Write JSON data safely with proper formatting."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error writing JSON to {filepath}: {e}")
        return False


def write_yaml_safely(filepath: str, data: Dict[str, Any]) -> bool:
    """Write YAML data safely with proper formatting."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
        return True
    except Exception as e:
        print(f"Error writing YAML to {filepath}: {e}")
        return False


def load_template(template_path: str) -> Optional[Dict[str, Any]]:
    """Load template file (JSON or YAML)."""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            if template_path.endswith('.yaml') or template_path.endswith('.yml'):
                return yaml.safe_load(f)
            elif template_path.endswith('.json'):
                return json.load(f)
    except Exception as e:
        print(f"Error loading template {template_path}: {e}")
        return None


def generate_diff(expected: Dict[str, Any], actual: Dict[str, Any], baseline_file: str, current_file: str) -> Dict[str, Any]:
    """Generate diff between expected and actual results."""
    mismatches = []
    
    def compare_values(exp, act, field_path=""):
        if type(exp) != type(act):
            mismatches.append({
                "field": field_path,
                "expected": exp,
                "actual": act
            })
        elif isinstance(exp, dict):
            for key in set(exp.keys()) | set(act.keys()):
                new_path = f"{field_path}.{key}" if field_path else key
                if key not in exp:
                    mismatches.append({
                        "field": new_path,
                        "expected": None,
                        "actual": act[key]
                    })
                elif key not in act:
                    mismatches.append({
                        "field": new_path,
                        "expected": exp[key],
                        "actual": None
                    })
                else:
                    compare_values(exp[key], act[key], new_path)
        elif isinstance(exp, list):
            if len(exp) != len(act):
                mismatches.append({
                    "field": f"{field_path}.count",
                    "expected": len(exp),
                    "actual": len(act)
                })
            for i, (exp_item, act_item) in enumerate(zip(exp, act)):
                compare_values(exp_item, act_item, f"{field_path}[{i}]")
        elif exp != act:
            mismatches.append({
                "field": field_path,
                "expected": exp,
                "actual": act
            })
    
    compare_values(expected, actual)
    
    return {
        "baseline_file": baseline_file,
        "current_file": current_file,
        "mismatches": mismatches
    }


def bump_version(version_str: str) -> str:
    """Bump version string (patch level)."""
    try:
        parts = version_str.split('.')
        if len(parts) >= 3:
            parts[2] = str(int(parts[2]) + 1)
        else:
            parts.append('1')
        return '.'.join(parts)
    except:
        return "0.1.1"


def check_constitution_compliance(target_path: str) -> bool:
    """Check if target path complies with constitution rules."""
    allowed_dirs = {'specs', 'baselines', 'logs', 'framework', 'docs'}
    
    # Normalize path to collapse relative components
    normalized_path = os.path.normpath(target_path)
    
    # Remove leading separator if present (cross-platform)
    if normalized_path.startswith(os.sep):
        normalized_path = normalized_path[len(os.sep):]
    
    # Extract first path component
    path_parts = normalized_path.split(os.sep)
    if not path_parts or not path_parts[0]:
        return False
    
    first_component = path_parts[0]
    
    return first_component in allowed_dirs


def load_critical_path_config(config_path: str = ".scraper-spec/config.yaml") -> List[str]:
    """Load critical path phases from config, fallback to defaults."""
    default_phases = ["Acquire", "Identify", "Collect", "Extract"]
    
    if not os.path.exists(config_path):
        return default_phases
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        if config and 'critical_path' in config and 'phases' in config['critical_path']:
            phases = config['critical_path']['phases']
            if isinstance(phases, list):
                # Return even if empty - this explicitly disables validation
                return phases
    except Exception as e:
        print(f"Warning: Could not load critical path config from {config_path}: {e}")
    
    return default_phases


def validate_critical_path_in_plan(plan_content: str, config_path: str = ".scraper-spec/config.yaml") -> tuple[bool, Optional[str]]:
    """Validate that all critical path phases appear in order in the plan.
    
    Returns:
        (is_valid, error_message): True with None if valid, False with error details if invalid
    """
    phases = load_critical_path_config(config_path)
    
    if not phases or len(phases) == 0:
        return True, None  # No phases to validate
    
    # Track which phases we've found and their positions
    found_positions = {}
    lines = plan_content.lower().split('\n')
    
    for idx, line in enumerate(lines):
        for phase in phases:
            if phase.lower() in line:
                if phase not in found_positions:
                    found_positions[phase] = idx
    
    # Check all phases are present
    missing_phases = [p for p in phases if p not in found_positions]
    if missing_phases:
        return False, f"Plan violates constitution (phase '{missing_phases[0]}' missing from critical path)"
    
    # Check phases appear in correct order
    phase_positions = [(phase, found_positions[phase]) for phase in phases]
    sorted_positions = sorted(phase_positions, key=lambda x: x[1])
    
    for i, phase in enumerate(phases):
        if sorted_positions[i][0] != phase:
            expected = phase
            actual = sorted_positions[i][0]
            return False, f"Plan violates constitution (phase '{actual}' appears before '{expected}' in critical path)"
    
    return True, None


def ensure_critical_path_in_plan(plan_content: str) -> bool:
    """Ensure critical path is preserved in plan (legacy compatibility)."""
    is_valid, _ = validate_critical_path_in_plan(plan_content)
    return is_valid


def log_action(action: str, site: str, details: str = "") -> None:
    """Log framework actions with timestamp."""
    timestamp = get_iso8601_timestamp()
    log_entry = f"[{timestamp}] {action} - Site: {site}"
    if details:
        log_entry += f" - {details}"
    print(log_entry)
