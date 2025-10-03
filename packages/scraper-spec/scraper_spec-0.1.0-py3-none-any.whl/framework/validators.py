"""
Schema validators for the scraper specification framework.
"""
import json
import yaml
import jsonschema
from typing import Dict, Any, Optional
import os


class FrameworkValidator:
    """Validates framework artifacts against templates."""
    
    def __init__(self, templates_dir: str = ".scraper-spec/templates"):
        self.templates_dir = templates_dir
        self._schemas = None  # Lazy-loaded
    
    @property
    def schemas(self):
        """Lazy-load schemas on first access."""
        if self._schemas is None:
            self._schemas = self._load_schemas()
        return self._schemas
    
    def _load_schemas(self) -> Dict[str, Dict[str, Any]]:
        """Load all template schemas."""
        schemas = {}
        
        # JSON schemas
        json_templates = ['baseline-template.json', 'log-template.json', 'diff-template.json', 'debug-log-template.json']
        for template in json_templates:
            schema = self._load_json_schema(template)
            if schema:
                schemas[template] = schema
        
        # YAML schemas
        yaml_templates = ['selectors-template.yaml']
        for template in yaml_templates:
            schema = self._load_yaml_schema(template)
            if schema:
                schemas[template] = schema
        
        return schemas
    
    def _load_json_schema(self, template_name: str) -> Optional[Dict[str, Any]]:
        """Load JSON template and convert to schema."""
        try:
            template_path = os.path.join(self.templates_dir, template_name)
            with open(template_path, 'r', encoding='utf-8') as f:
                template = json.load(f)
            return self._json_to_schema(template)
        except Exception as e:
            print(f"Error loading JSON template {template_name}: {e}")
            return None
    
    def _load_yaml_schema(self, template_name: str) -> Optional[Dict[str, Any]]:
        """Load YAML template and convert to schema."""
        try:
            template_path = os.path.join(self.templates_dir, template_name)
            with open(template_path, 'r', encoding='utf-8') as f:
                template = yaml.safe_load(f)
            return self._yaml_to_schema(template)
        except Exception as e:
            print(f"Error loading YAML template {template_name}: {e}")
            return None
    
    def _json_to_schema(self, template: Dict[str, Any]) -> Dict[str, Any]:
        """Convert JSON template to JSON schema."""
        def infer_type(value):
            if isinstance(value, dict):
                properties = {}
                for k, v in value.items():
                    properties[k] = infer_type(v)
                return {
                    "type": "object",
                    "properties": properties,
                    "required": list(value.keys())
                }
            elif isinstance(value, list):
                if value:
                    return {
                        "type": "array",
                        "items": infer_type(value[0])
                    }
                return {"type": "array"}
            elif isinstance(value, str):
                return {"type": "string"}
            elif isinstance(value, int):
                return {"type": "integer"}
            elif isinstance(value, float):
                return {"type": "number"}
            elif isinstance(value, bool):
                return {"type": "boolean"}
            else:
                return {"type": "string"}
        
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            **infer_type(template)
        }
    
    def _yaml_to_schema(self, template: Dict[str, Any]) -> Dict[str, Any]:
        """Convert YAML template to schema."""
        # For YAML, we'll use a simplified validation approach
        def get_required_keys(obj, path=""):
            required = []
            if isinstance(obj, dict):
                for key, value in obj.items():
                    current_path = f"{path}.{key}" if path else key
                    required.append(current_path)
                    if isinstance(value, dict):
                        required.extend(get_required_keys(value, current_path))
            return required
        
        return {
            "type": "yaml",
            "required_keys": get_required_keys(template)
        }
    
    def validate_selectors_yaml(self, data: Dict[str, Any]) -> bool:
        """Validate selectors YAML against template."""
        try:
            template_name = 'selectors-template.yaml'
            if template_name not in self.schemas:
                print(f"Schema for {template_name} not found")
                return False
            
            schema = self.schemas[template_name]
            required_keys = schema.get('required_keys', [])
            
            def check_keys(obj, path=""):
                for key in required_keys:
                    if path and not key.startswith(path):
                        continue
                    
                    key_parts = key.split('.')
                    current = obj
                    
                    for part in key_parts:
                        if isinstance(current, dict) and part in current:
                            current = current[part]
                        else:
                            print(f"Missing required key: {key}")
                            return False
                return True
            
            return check_keys(data)
        except Exception as e:
            print(f"YAML validation error: {e}")
            return False
    
    def validate_baseline_json(self, data: Dict[str, Any]) -> bool:
        """Validate baseline JSON against template."""
        return self._validate_json(data, 'baseline-template.json')
    
    def validate_log_json(self, data: Dict[str, Any]) -> bool:
        """Validate log JSON against template."""
        return self._validate_json(data, 'log-template.json')
    
    def validate_diff_json(self, data: Dict[str, Any]) -> bool:
        """Validate diff JSON against template."""
        return self._validate_json(data, 'diff-template.json')
    
    def validate_debug_log_json(self, data: Dict[str, Any]) -> bool:
        """Validate debug log JSON against template."""
        return self._validate_json(data, 'debug-log-template.json')
    
    def _validate_json(self, data: Dict[str, Any], template_name: str) -> bool:
        """Validate JSON data against schema."""
        try:
            if template_name not in self.schemas:
                print(f"Schema for {template_name} not found")
                return False
            
            schema = self.schemas[template_name]
            jsonschema.validate(data, schema)
            return True
        except jsonschema.ValidationError as e:
            print(f"JSON validation error for {template_name}: {e.message}")
            return False
        except Exception as e:
            print(f"Validation error: {e}")
            return False
    
    def validate_file(self, filepath: str, template_type: str) -> bool:
        """Validate file against appropriate template."""
        try:
            if template_type == 'selectors':
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                return self.validate_selectors_yaml(data)
            elif template_type == 'baseline':
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return self.validate_baseline_json(data)
            elif template_type == 'log':
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return self.validate_log_json(data)
            elif template_type == 'diff':
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return self.validate_diff_json(data)
            elif template_type == 'debug-log':
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return self.validate_debug_log_json(data)
            else:
                print(f"Unknown template type: {template_type}")
                return False
        except Exception as e:
            print(f"Error validating file {filepath}: {e}")
            return False
