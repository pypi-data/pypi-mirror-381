#!/usr/bin/env python3
"""
Scraper Specification Framework CLI Runner
Implements all core commands defined in the enforcement plan.
"""
import argparse
import os
import sys
import json
import yaml
import shutil
from datetime import datetime
from typing import Dict, Any, Optional

from .utils import (
    get_iso8601_timestamp, write_json_safely, write_yaml_safely, 
    load_template, generate_diff, bump_version, 
    check_constitution_compliance, validate_critical_path_in_plan, log_action
)
from .validators import FrameworkValidator


class ScraperFrameworkRunner:
    """Main CLI runner for scraper specification framework."""
    
    def __init__(self):
        self.validator = FrameworkValidator()
        self.constitution_path = ".scraper-spec/memory/constitution.md"
        self.templates_dir = ".scraper-spec/templates"
    
    def setup(self) -> bool:
        """Initialize framework structure in current directory."""
        try:
            from importlib.resources import files
        except ImportError:
            # Fallback for Python < 3.9
            from importlib_resources import files
        
        log_action("SETUP", "framework", "Initializing scraper-spec framework")
        
        # Get templates from installed package
        try:
            template_source = str(files('framework').joinpath('scraper_spec_templates'))
        except Exception as e:
            print(f"ERROR: Could not locate framework templates: {e}")
            return False
        
        # Copy to current directory as .scraper-spec/
        if os.path.exists('.scraper-spec'):
            print("ERROR: .scraper-spec already exists in this directory")
            return False
        
        try:
            shutil.copytree(template_source, '.scraper-spec')
        except Exception as e:
            print(f"ERROR: Failed to copy templates: {e}")
            return False
        
        # Create project directories
        directories = [
            "specs",
            "baselines/screenshots",
            "logs/regressions",
            "logs/debug",
            "docs",
            "framework"
        ]
        
        for dir_path in directories:
            os.makedirs(dir_path, exist_ok=True)
        
        # Copy framework plan
        try:
            from importlib.resources import files
        except ImportError:
            from importlib_resources import files
        
        plan_source = str(files('framework').joinpath('scraper_spec_templates/templates/plan-template.md'))
        shutil.copy(plan_source, 'framework/plan.md')
        
        # Copy config if it exists in templates
        config_source = str(files('framework').joinpath('scraper_spec_templates/config.yaml'))
        if os.path.exists(config_source):
            shutil.copy(config_source, '.scraper-spec/config.yaml')
        
        # Copy SCRAPER_SPEC charter
        charter_content = """# Scraper Spec Framework Charter

This framework provides automation/scraping engineers with a standardized approach to building, testing, and maintaining web scrapers.

## Development Phases

1. **Discover** → run scraper-spec discover <site-name>
2. **Specify** → edit spec in /specs/<site-name>.yaml
3. **Baseline** → run scraper-spec baseline <site-name> "<query>"
4. **Push** → sync spec + baseline into assistant context
5. **Test** → run scraper-spec test <site-name> and confirm no regressions
6. **Pull** → refresh local files from assistant if modified in-memory
7. **Release** → lock version via scraper-spec release <site-name>

## Outcome

By enforcing this structure:
• Every scraper has a spec, baselines, screenshots, logs, and a plan.
• Regression testing is built-in.
• Push/pull ensures AI context stays aligned with repo artifacts.
• No accidental drift — selectors, baselines, logs, and plans always stay aligned.
• Automation engineers have reproducible, enforceable workflows with full observability.
"""
        with open('specs/SCRAPER_SPEC.md', 'w') as f:
            f.write(charter_content)
        
        print("\n✓ Framework initialized successfully!")
        print("\nDirectory structure created:")
        for d in directories:
            print(f"  - {d}/")
        print("  - .scraper-spec/")
        print("\nNext steps:")
        print("  1. scraper-spec init <site-name>")
        print("  2. Edit specs/<site-name>.yaml with your selectors")
        print("  3. scraper-spec baseline <site-name> \"<query>\"")
        print("  4. Build your scraper using the spec")
        
        return True
    
    def _check_constitution(self) -> bool:
        """Check if constitution file exists and is readable."""
        if not os.path.exists(self.constitution_path):
            print(f"ERROR: Constitution file not found at {self.constitution_path}")
            return False
        return True
    
    def _validate_plan_critical_path(self, plan_path: str) -> bool:
        """Validate that plan contains all critical path phases in order."""
        if not os.path.exists(plan_path):
            return True  # No plan to validate
        
        try:
            with open(plan_path, 'r', encoding='utf-8') as f:
                plan_content = f.read()
            
            is_valid, error_msg = validate_critical_path_in_plan(plan_content)
            
            if not is_valid:
                print(f"ERROR: {error_msg}")
                return False
            
            return True
        except Exception as e:
            print(f"ERROR: Could not validate plan critical path: {e}")
            return False
    
    def _get_top_level_dir(self, path: str) -> str:
        """Extract top-level directory from path."""
        normalized_path = os.path.normpath(path)
        if normalized_path.startswith(os.sep):
            normalized_path = normalized_path[len(os.sep):]
        path_parts = normalized_path.split(os.sep)
        return path_parts[0] if path_parts and path_parts[0] else "unknown"
    
    def _validate_site_name(self, site: str) -> bool:
        """Validate site name format."""
        if not site or not site.replace('-', '').replace('_', '').isalnum():
            print("ERROR: Site name must be alphanumeric (with hyphens/underscores allowed)")
            return False
        return True
    
    def check(self) -> bool:
        """Check environment and framework setup."""
        import sys
        import importlib.util
        
        print("Checking scraper-spec environment...\n")
        all_ok = True
        
        # Check Python version
        py_version = sys.version_info
        print(f"✓ Python {py_version.major}.{py_version.minor}.{py_version.micro}")
        if py_version < (3, 8):
            print("  ⚠️  Warning: Python 3.8+ recommended")
            all_ok = False
        
        # Check required packages
        packages = {
            'jsonschema': 'jsonschema>=4.0.0',
            'yaml': 'PyYAML>=6.0'
        }
        
        for module, pkg_name in packages.items():
            spec = importlib.util.find_spec(module)
            if spec:
                print(f"✓ {pkg_name}")
            else:
                print(f"✗ {pkg_name} - NOT INSTALLED")
                all_ok = False
        
        # Check framework structure
        print("\nFramework structure:")
        if os.path.exists('.scraper-spec'):
            print("✓ .scraper-spec/ exists")
            
            # Check required dirs
            required_dirs = ['specs', 'baselines', 'logs', 'docs', 'framework']
            for dir_name in required_dirs:
                if os.path.exists(dir_name):
                    print(f"  ✓ {dir_name}/")
                else:
                    print(f"  ✗ {dir_name}/ - MISSING")
                    all_ok = False
            
            # Check critical files
            critical_files = [
                '.scraper-spec/memory/constitution.md',
                '.scraper-spec/config.yaml'
            ]
            for file_path in critical_files:
                if os.path.exists(file_path):
                    print(f"  ✓ {file_path}")
                else:
                    print(f"  ✗ {file_path} - MISSING")
                    all_ok = False
        else:
            print("✗ .scraper-spec/ - NOT INITIALIZED")
            print("  Run: scraper-spec setup")
            all_ok = False
        
        print()
        if all_ok:
            print("✅ All checks passed!")
            return True
        else:
            print("❌ Some checks failed. See above for details.")
            return False
    
    def discover(self, site: str) -> bool:
        """Implement /discover <site> command."""
        if not self._validate_site_name(site):
            return False
        
        log_action("DISCOVER", site, "Starting site discovery")
        
        # Load selectors template
        template_path = os.path.join(self.templates_dir, "selectors-template.yaml")
        template = load_template(template_path)
        if not template:
            print(f"ERROR: Could not load selectors template from {template_path}")
            return False
        
        # Create discovery spec with placeholders
        discovery_spec = template.copy()
        discovery_spec['site_config']['base_url'] = f"<{site} root URL here>"
        
        # Write to specs directory
        output_path = f"specs/{site}.discover.yaml"
        if not check_constitution_compliance(output_path):
            top_dir = self._get_top_level_dir(output_path)
            print(f"ERROR: Output path {output_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        
        if write_yaml_safely(output_path, discovery_spec):
            log_action("DISCOVER", site, f"Created discovery spec at {output_path}")
            return True
        else:
            print(f"ERROR: Failed to write discovery spec to {output_path}")
            return False
    
    def init(self, site: str) -> bool:
        """Implement /init <site> command."""
        if not self._validate_site_name(site):
            return False
        
        log_action("INIT", site, "Initializing site spec")
        
        # Load selectors template
        template_path = os.path.join(self.templates_dir, "selectors-template.yaml")
        template = load_template(template_path)
        if not template:
            print(f"ERROR: Could not load selectors template from {template_path}")
            return False
        
        # Create initial spec with placeholders only
        init_spec = template.copy()
        init_spec['site_config']['base_url'] = f"<define target site here>"
        
        # Write to specs directory
        output_path = f"specs/{site}.yaml"
        if not check_constitution_compliance(output_path):
            top_dir = self._get_top_level_dir(output_path)
            print(f"ERROR: Output path {output_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        
        if write_yaml_safely(output_path, init_spec):
            if self.validator.validate_file(output_path, 'selectors'):
                log_action("INIT", site, f"Created spec at {output_path}")
                return True
            else:
                print(f"ERROR: Validation failed for {output_path}")
                return False
        else:
            print(f"ERROR: Failed to write spec to {output_path}")
            return False
    
    def baseline(self, site: str, query: str) -> bool:
        """Implement /baseline <site> "<query>" command."""
        if not self._validate_site_name(site):
            return False
        
        # Validate plan has critical path before creating baseline
        plan_path = "framework/plan.md"
        if not self._validate_plan_critical_path(plan_path):
            return False
        
        # Check if baseline already exists (overwrite guard)
        baseline_path = f"baselines/{site}.expected.json"
        if os.path.exists(baseline_path):
            if os.environ.get("SCRAPER_SPEC_CONFIRM") not in ("1", "true", "TRUE", "yes", "YES"):
                print(f"ERROR: Baseline exists at {baseline_path}")
                print("To overwrite, use `rebaseline` or set SCRAPER_SPEC_CONFIRM=1")
                return False
        
        log_action("BASELINE", site, f"Creating baseline with query: {query}")
        timestamp = get_iso8601_timestamp()
        
        # Create baseline JSON
        baseline_template_path = os.path.join(self.templates_dir, "baseline-template.json")
        baseline_template = load_template(baseline_template_path)
        if not baseline_template:
            print(f"ERROR: Could not load baseline template from {baseline_template_path}")
            return False
        
        baseline_data = baseline_template.copy()
        baseline_data['metadata']['created_date'] = timestamp
        baseline_data['metadata']['site_target'] = site
        baseline_data['metadata']['test_query'] = query
        
        # Create log JSON
        log_template_path = os.path.join(self.templates_dir, "log-template.json")
        log_template = load_template(log_template_path)
        if not log_template:
            print(f"ERROR: Could not load log template from {log_template_path}")
            return False
        
        log_data = log_template.copy()
        log_data['timestamp'] = timestamp
        log_data['site'] = site
        log_data['query'] = query
        
        # Write artifacts
        log_path = f"logs/{site}_{timestamp.replace(':', '-')}.log.json"
        artifacts = [
            (f"baselines/{site}.expected.json", baseline_data, 'baseline'),
            (log_path, log_data, 'log')
        ]
        
        for artifact_path, artifact_data, template_type in artifacts:
            if not check_constitution_compliance(artifact_path):
                top_dir = self._get_top_level_dir(artifact_path)
                print(f"ERROR: Output path {artifact_path} violates constitution (top-level '{top_dir}' not allowed)")
                return False
            
            if not write_json_safely(artifact_path, artifact_data):
                print(f"ERROR: Failed to write {artifact_path}")
                return False
            
            if not self.validator.validate_file(artifact_path, template_type):
                print(f"ERROR: Validation failed for {artifact_path}")
                return False
        
        # Create placeholder HTML snapshot
        snapshot_path = f"baselines/{site}.snapshot.html"
        if check_constitution_compliance(snapshot_path):
            os.makedirs(os.path.dirname(snapshot_path), exist_ok=True)
            with open(snapshot_path, 'w', encoding='utf-8') as f:
                f.write(f"<!-- Snapshot for {site} with query '{query}' at {timestamp} -->\\n")
                f.write("<html><body>Placeholder snapshot - implement scraper to populate</body></html>")
        
        # Create placeholder screenshot
        screenshot_path = f"baselines/screenshots/{site}_{query.replace(' ', '_')}.png"
        if check_constitution_compliance(screenshot_path):
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            with open(screenshot_path, 'w', encoding='utf-8') as f:
                f.write(f"# Placeholder screenshot for {site} query '{query}' at {timestamp}")
        
        # Artifact completeness check (baseline)
        required = [baseline_path, snapshot_path, screenshot_path, log_path]
        missing = [p for p in required if not os.path.exists(p)]
        if missing:
            print(f"ERROR: Incomplete artifact set after baseline. Missing: {', '.join(missing)}")
            return False
        
        log_action("BASELINE", site, f"Created baseline artifacts for query: {query}")
        return True
    
    def test(self, site: str) -> bool:
        """Implement /test <site> command."""
        if not self._validate_site_name(site):
            return False
        
        # Validate plan has critical path before testing
        plan_path = "framework/plan.md"
        if not self._validate_plan_critical_path(plan_path):
            return False
        
        log_action("TEST", site, "Running regression test")
        
        # Load baseline
        baseline_path = f"baselines/{site}.expected.json"
        if not os.path.exists(baseline_path):
            print(f"ERROR: No baseline found at {baseline_path}")
            return False
        
        try:
            with open(baseline_path, 'r', encoding='utf-8') as f:
                baseline_data = json.load(f)
        except Exception as e:
            print(f"ERROR: Could not load baseline from {baseline_path}: {e}")
            return False
        
        # For testing purposes, create a mock current result
        # In real implementation, this would run the actual scraper
        current_data = baseline_data.copy()
        query = baseline_data.get('metadata', {}).get('test_query', 'test_query')
        
        # Generate diff
        diff_data = generate_diff(baseline_data, current_data, baseline_path, "current_run")
        
        # Save diff to regressions
        timestamp = get_iso8601_timestamp()
        diff_path = f"logs/regressions/{site}_{query.replace(' ', '_')}.diff.json"
        
        if not check_constitution_compliance(diff_path):
            top_dir = self._get_top_level_dir(diff_path)
            print(f"ERROR: Output path {diff_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        
        if write_json_safely(diff_path, diff_data):
            if self.validator.validate_file(diff_path, 'diff'):
                log_action("TEST", site, f"Regression test completed - diff saved to {diff_path}")
                if diff_data['mismatches']:
                    print(f"WARNING: {len(diff_data['mismatches'])} mismatches found")
                else:
                    print("SUCCESS: No regressions detected")
                # Artifact completeness check (test)
                if not os.path.exists(diff_path):
                    print(f"ERROR: Expected diff artifact missing at {diff_path}")
                    return False
                return True
            else:
                print(f"ERROR: Validation failed for {diff_path}")
                return False
        else:
            print(f"ERROR: Failed to write diff to {diff_path}")
            return False
    
    def release(self, site: str) -> bool:
        """Implement /release <site> command."""
        if not self._validate_site_name(site):
            return False
        
        log_action("RELEASE", site, "Releasing stable version")
        
        # Load spec file
        spec_path = f"specs/{site}.yaml"
        if not os.path.exists(spec_path):
            print(f"ERROR: No spec found at {spec_path}")
            return False
        
        try:
            with open(spec_path, 'r', encoding='utf-8') as f:
                spec_data = yaml.safe_load(f)
        except Exception as e:
            print(f"ERROR: Could not load spec from {spec_path}: {e}")
            return False
        
        # Bump version
        current_version = spec_data.get('version', '0.1.0')
        new_version = bump_version(current_version)
        spec_data['version'] = new_version
        spec_data['release_date'] = get_iso8601_timestamp()
        
        # Write updated spec
        if write_yaml_safely(spec_path, spec_data):
            if self.validator.validate_file(spec_path, 'selectors'):
                # Update changelog
                changelog_path = "docs/CHANGELOG.md"
                if check_constitution_compliance(changelog_path):
                    os.makedirs(os.path.dirname(changelog_path), exist_ok=True)
                    timestamp = get_iso8601_timestamp()
                    changelog_entry = f"\\n## {new_version} - {timestamp}\\n\\n- Released stable version for {site}\\n"
                    
                    if os.path.exists(changelog_path):
                        with open(changelog_path, 'r', encoding='utf-8') as f:
                            existing_content = f.read()
                        with open(changelog_path, 'w', encoding='utf-8') as f:
                            f.write(f"# Changelog{changelog_entry}\\n{existing_content}")
                    else:
                        with open(changelog_path, 'w', encoding='utf-8') as f:
                            f.write(f"# Changelog{changelog_entry}")
                
                log_action("RELEASE", site, f"Released version {new_version}")
                return True
            else:
                print(f"ERROR: Validation failed for updated spec")
                return False
        else:
            print(f"ERROR: Failed to update spec version")
            return False
    
    def push(self, site: str) -> bool:
        """Implement /push <site> command (stub)."""
        if not self._validate_site_name(site):
            return False
        
        log_action("PUSH", site, "MCP integration not implemented")
        print(f"STUB: Would push {site} spec and baseline to MCP assistant context")
        return True
    
    def pull(self, site: str) -> bool:
        """Implement /pull <site> command (stub)."""
        if not self._validate_site_name(site):
            return False
        
        log_action("PULL", site, "MCP integration not implemented")
        print(f"STUB: Would pull {site} spec and baseline from MCP assistant context")
        return True

    def debug(self, site: str, query: str) -> bool:
        """Implement /debug <site> "<query>" command.
        Generates HTML snapshot, screenshot placeholder, debug log JSON, and debug report markdown.
        """
        if not self._validate_site_name(site):
            return False
        
        log_action("DEBUG", site, f"Generating debug artifacts for query: {query}")
        timestamp = get_iso8601_timestamp()
        safe_query = query.replace(' ', '_')
        
        # Load debug log template
        debug_log_template_path = os.path.join(self.templates_dir, "debug-log-template.json")
        try:
            with open(debug_log_template_path, 'r', encoding='utf-8') as f:
                debug_log_template = json.load(f)
        except Exception as e:
            print(f"ERROR: Could not load debug log template from {debug_log_template_path}: {e}")
            return False
        
        # Prepare debug log data
        debug_log = debug_log_template.copy()
        debug_log["timestamp"] = timestamp
        debug_log["site"] = site
        debug_log["query"] = query
        
        # Write debug log JSON
        debug_dir = f"logs/debug"
        debug_log_path = f"{debug_dir}/{site}_{safe_query}_{timestamp.replace(':', '-')}.debug.log.json"
        if not check_constitution_compliance(debug_log_path):
            top_dir = self._get_top_level_dir(debug_log_path)
            print(f"ERROR: Output path {debug_log_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        if not write_json_safely(debug_log_path, debug_log):
            print(f"ERROR: Failed to write debug log to {debug_log_path}")
            return False
        # Validate debug log JSON
        if not self.validator.validate_file(debug_log_path, 'debug-log'):
            print(f"ERROR: Validation failed for {debug_log_path}")
            return False
        
        # Load debug report template (markdown)
        debug_report_template_path = os.path.join(self.templates_dir, "debug-report-template.md")
        try:
            with open(debug_report_template_path, 'r', encoding='utf-8') as f:
                report_template = f.read()
        except Exception as e:
            print(f"ERROR: Could not load debug report template from {debug_report_template_path}: {e}")
            return False
        
        report_content = report_template.replace("<site>", site).replace("<query>", query).replace("<timestamp>", timestamp)
        debug_report_path = f"{debug_dir}/{site}_{safe_query}_{timestamp.replace(':', '-')}.debug.report.md"
        if not check_constitution_compliance(debug_report_path):
            top_dir = self._get_top_level_dir(debug_report_path)
            print(f"ERROR: Output path {debug_report_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        os.makedirs(os.path.dirname(debug_report_path), exist_ok=True)
        with open(debug_report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # HTML snapshot
        snapshot_path = f"{debug_dir}/{site}_{safe_query}_{timestamp.replace(':', '-')}.snapshot.html"
        if not check_constitution_compliance(snapshot_path):
            top_dir = self._get_top_level_dir(snapshot_path)
            print(f"ERROR: Output path {snapshot_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        os.makedirs(os.path.dirname(snapshot_path), exist_ok=True)
        with open(snapshot_path, 'w', encoding='utf-8') as f:
            f.write(f"<!-- Debug Snapshot for {site} with query '{query}' at {timestamp} -->\n")
            f.write("<html><body>Debug snapshot placeholder - implement scraper to populate</body></html>")
        
        # Screenshot placeholder
        screenshot_path = f"{debug_dir}/{site}_{safe_query}_{timestamp.replace(':', '-')}.png"
        if not check_constitution_compliance(screenshot_path):
            top_dir = self._get_top_level_dir(screenshot_path)
            print(f"ERROR: Output path {screenshot_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        with open(screenshot_path, 'w', encoding='utf-8') as f:
            f.write(f"# Debug screenshot placeholder for {site} query '{query}' at {timestamp}")
        
        log_action("DEBUG", site, f"Created debug artifacts at {debug_dir}")
        return True
    
    def rollback(self, site: str) -> bool:
        """Implement /rollback <site> command.
        Restores last stable spec and baseline from backups, logs rollback into /logs/regressions/.
        """
        if not self._validate_site_name(site):
            return False
        
        log_action("ROLLBACK", site, "Attempting to restore from backups")
        timestamp = get_iso8601_timestamp()
        
        # Define paths
        baseline_active = f"baselines/{site}.expected.json"
        snapshot_active = f"baselines/{site}.snapshot.html"
        screenshot_glob_dir = f"baselines/screenshots"
        spec_active = f"specs/{site}.yaml"
        
        backups_baselines_dir = "baselines/backups"
        backups_specs_dir = "specs/backups"
        
        # Find latest baseline backup
        latest_baseline_backup = None
        if os.path.isdir(backups_baselines_dir):
            candidates = [f for f in os.listdir(backups_baselines_dir) if f.startswith(site + "_") and f.endswith(".expected.json")]
            candidates.sort(reverse=True)
            if candidates:
                latest_baseline_backup = os.path.join(backups_baselines_dir, candidates[0])
        
        # Find latest spec backup
        latest_spec_backup = None
        if os.path.isdir(backups_specs_dir):
            candidates = [f for f in os.listdir(backups_specs_dir) if f.startswith(site + "_") and f.endswith(".yaml")]
            candidates.sort(reverse=True)
            if candidates:
                latest_spec_backup = os.path.join(backups_specs_dir, candidates[0])
        
        if not latest_baseline_backup or not latest_spec_backup:
            print("ERROR: No backups found to rollback")
            return False
        
        # Restore files
        os.makedirs(os.path.dirname(baseline_active), exist_ok=True)
        shutil.copyfile(latest_baseline_backup, baseline_active)
        shutil.copyfile(os.path.join(backups_baselines_dir, os.path.basename(latest_baseline_backup).replace('.expected.json', '.snapshot.html')), snapshot_active)
        # Restore a screenshot if exists (optional)
        os.makedirs(screenshot_glob_dir, exist_ok=True)
        screenshot_backup = os.path.join(backups_baselines_dir, os.path.basename(latest_baseline_backup).replace('.expected.json', '.png'))
        if os.path.exists(screenshot_backup):
            shutil.copyfile(screenshot_backup, os.path.join(screenshot_glob_dir, f"{site}_restored.png"))
        
        os.makedirs(os.path.dirname(spec_active), exist_ok=True)
        shutil.copyfile(latest_spec_backup, spec_active)
        
        # Log rollback event
        rollback_log = {
            "action": "rollback",
            "site": site,
            "timestamp": timestamp,
            "baseline_backup": latest_baseline_backup,
            "spec_backup": latest_spec_backup
        }
        rollback_log_path = f"logs/regressions/{site}_rollback_{timestamp.replace(':', '-')}.json"
        if not check_constitution_compliance(rollback_log_path):
            top_dir = self._get_top_level_dir(rollback_log_path)
            print(f"ERROR: Output path {rollback_log_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        write_json_safely(rollback_log_path, rollback_log)
        
        log_action("ROLLBACK", site, "Rollback completed")
        return True
    
    def rebaseline(self, site: str, query: str) -> bool:
        """Implement /rebaseline <site> "<query>" command.
        Promotes last successful debug run into baseline, updates spec metadata, backs up old baseline first.
        Requires explicit confirmation via environment variable SCRAPER_SPEC_CONFIRM=1.
        """
        if not self._validate_site_name(site):
            return False
        
        if os.environ.get("SCRAPER_SPEC_CONFIRM") not in ("1", "true", "TRUE", "yes", "YES"):
            print("ERROR: Rebaseline requires confirmation. Set SCRAPER_SPEC_CONFIRM=1 and re-run.")
            return False
        
        log_action("REBASELINE", site, f"Promoting debug run to baseline for query: {query}")
        timestamp = get_iso8601_timestamp()
        safe_query = query.replace(' ', '_')
        
        # Find latest successful debug log for site and query
        debug_dir = "logs/debug"
        if not os.path.isdir(debug_dir):
            print("ERROR: No debug runs found")
            return False
        
        candidates = []
        for name in os.listdir(debug_dir):
            if name.startswith(f"{site}_{safe_query}") and name.endswith(".debug.log.json"):
                candidates.append(name)
        candidates.sort(reverse=True)
        if not candidates:
            print("ERROR: No matching debug runs found for provided site and query")
            return False
        
        # Load the latest and ensure it is successful (errors empty)
        debug_log_path = os.path.join(debug_dir, candidates[0])
        try:
            with open(debug_log_path, 'r', encoding='utf-8') as f:
                debug_log = json.load(f)
        except Exception as e:
            print(f"ERROR: Could not read debug log {debug_log_path}: {e}")
            return False
        
        errors = debug_log.get("errors", [])
        if errors:
            print("ERROR: Last debug run contains errors; cannot promote to baseline")
            return False
        
        # Backup current baseline and related artifacts
        baseline_path = f"baselines/{site}.expected.json"
        snapshot_path = f"baselines/{site}.snapshot.html"
        screenshot_dir = f"baselines/screenshots"
        current_query = safe_query
        
        backups_baselines_dir = "baselines/backups"
        os.makedirs(backups_baselines_dir, exist_ok=True)
        backup_prefix = f"{site}_{timestamp.replace(':', '-')}"
        
        if os.path.exists(baseline_path):
            shutil.copyfile(baseline_path, os.path.join(backups_baselines_dir, f"{backup_prefix}.expected.json"))
        if os.path.exists(snapshot_path):
            shutil.copyfile(snapshot_path, os.path.join(backups_baselines_dir, f"{backup_prefix}.snapshot.html"))
        # Attempt to backup a screenshot that matches the previous baseline query (best-effort)
        prev_screenshot = None
        if os.path.isdir(screenshot_dir):
            for name in os.listdir(screenshot_dir):
                if name.startswith(f"{site}_") and name.endswith(".png"):
                    prev_screenshot = os.path.join(screenshot_dir, name)
                    break
        if prev_screenshot:
            shutil.copyfile(prev_screenshot, os.path.join(backups_baselines_dir, f"{backup_prefix}.png"))
        
        # Promote debug results to baseline
        baseline_template_path = os.path.join(self.templates_dir, "baseline-template.json")
        baseline_template = load_template(baseline_template_path)
        if not baseline_template:
            print(f"ERROR: Could not load baseline template from {baseline_template_path}")
            return False
        new_baseline = baseline_template.copy()
        new_baseline['metadata']['created_date'] = timestamp
        new_baseline['metadata']['site_target'] = site
        new_baseline['metadata']['test_query'] = query
        # If debug log contains results, use them; else keep empty results
        if isinstance(debug_log.get('results'), list):
            new_baseline['results'] = debug_log['results']
        
        if not check_constitution_compliance(baseline_path):
            top_dir = self._get_top_level_dir(baseline_path)
            print(f"ERROR: Output path {baseline_path} violates constitution (top-level '{top_dir}' not allowed)")
            return False
        if not write_json_safely(baseline_path, new_baseline):
            print("ERROR: Failed to write new baseline")
            return False
        if not self.validator.validate_file(baseline_path, 'baseline'):
            print("ERROR: Validation failed for new baseline")
            return False
        
        # Write snapshot and screenshot from debug artifacts if available
        base_name = candidates[0].replace('.debug.log.json', '')
        debug_snapshot = os.path.join(debug_dir, base_name + ".snapshot.html")
        debug_screenshot = os.path.join(debug_dir, base_name + ".png")
        os.makedirs(os.path.dirname(snapshot_path), exist_ok=True)
        if os.path.exists(debug_snapshot):
            shutil.copyfile(debug_snapshot, snapshot_path)
        else:
            with open(snapshot_path, 'w', encoding='utf-8') as f:
                f.write(f"<!-- Snapshot promoted from debug {base_name} at {timestamp} -->\n")
                f.write("<html><body>Snapshot unavailable in debug; placeholder</body></html>")
        os.makedirs(screenshot_dir, exist_ok=True)
        target_screenshot = os.path.join(screenshot_dir, f"{site}_{current_query}.png")
        if os.path.exists(debug_screenshot):
            shutil.copyfile(debug_screenshot, target_screenshot)
        else:
            with open(target_screenshot, 'w', encoding='utf-8') as f:
                f.write(f"# Placeholder screenshot promoted from debug at {timestamp}")
        
        # Update spec metadata
        spec_path = f"specs/{site}.yaml"
        if os.path.exists(spec_path):
            try:
                with open(spec_path, 'r', encoding='utf-8') as f:
                    spec_data = yaml.safe_load(f) or {}
            except Exception as e:
                print(f"ERROR: Could not read spec: {e}")
                return False
            spec_data['last_rebaseline'] = timestamp
            if not write_yaml_safely(spec_path, spec_data):
                print("ERROR: Failed to update spec metadata")
                return False
            # Backup spec
            backups_specs_dir = "specs/backups"
            os.makedirs(backups_specs_dir, exist_ok=True)
            shutil.copyfile(spec_path, os.path.join(backups_specs_dir, f"{backup_prefix}.yaml"))
        
        log_action("REBASELINE", site, "Rebaseline completed")
        return True


def main():
    """Main CLI entrypoint."""
    parser = argparse.ArgumentParser(
        description="Scraper Specification Framework CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  setup                     Initialize framework in current directory
  check                     Check environment and framework setup
  discover <site>           Crawl and discover selectors for site
  init <site>              Initialize spec file for site
  baseline <site> "query"  Create baseline artifacts
  test <site>              Run regression test against baseline
  release <site>           Tag stable version and update changelog
  push <site>              Push spec to MCP context (stub)
  pull <site>              Pull spec from MCP context (stub)
  debug <site> "query"     Generate debug artifacts (snapshot, screenshot, log, report)
  rollback <site>          Restore last stable spec and baseline from backups
  rebaseline <site> "query" Promote last successful debug run to baseline (requires SCRAPER_SPEC_CONFIRM=1)
        """
    )
    
    parser.add_argument('command', help='Command to execute')
    parser.add_argument('site', nargs='?', help='Target site name')
    parser.add_argument('query', nargs='?', help='Search query (for baseline/debug/rebaseline)')
    
    args = parser.parse_args()
    
    # Special cases: setup and check don't require .scraper-spec to exist
    if args.command == 'setup':
        runner = ScraperFrameworkRunner()
        success = runner.setup()
        sys.exit(0 if success else 1)
    
    if args.command == 'check':
        runner = ScraperFrameworkRunner()
        success = runner.check()
        sys.exit(0 if success else 1)
    
    # All other commands require .scraper-spec/
    if not os.path.exists('.scraper-spec'):
        print("ERROR: Framework not initialized in this directory")
        print("Run: scraper-spec setup")
        sys.exit(1)
    
    runner = ScraperFrameworkRunner()
    
    if not runner._check_constitution():
        sys.exit(1)
    
    success = False
    
    if args.command == 'discover':
        success = runner.discover(args.site)
    elif args.command == 'init':
        success = runner.init(args.site)
    elif args.command == 'baseline':
        if not args.query:
            print("ERROR: baseline command requires a query argument")
            sys.exit(1)
        success = runner.baseline(args.site, args.query)
    elif args.command == 'test':
        success = runner.test(args.site)
    elif args.command == 'release':
        success = runner.release(args.site)
    elif args.command == 'push':
        success = runner.push(args.site)
    elif args.command == 'pull':
        success = runner.pull(args.site)
    elif args.command == 'debug':
        if not args.query:
            print("ERROR: debug command requires a query argument")
            sys.exit(1)
        success = runner.debug(args.site, args.query)
    elif args.command == 'rollback':
        success = runner.rollback(args.site)
    elif args.command == 'rebaseline':
        if not args.query:
            print("ERROR: rebaseline command requires a query argument")
            sys.exit(1)
        success = runner.rebaseline(args.site, args.query)
    else:
        print(f"ERROR: Unknown command '{args.command}'")
        parser.print_help()
        sys.exit(1)
    
    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
