# scraping-spec-kit

A comprehensive toolkit for web scraping specifications and automation

## What This Is

A governance and testing framework that helps automation engineers:

- Standardize scraper configurations
- Manage baselines and detect regressions
- Enforce best practices via constitutional rules
- Track versions and maintain audit trails

**This is NOT a scraping library.** It's a spec kit that works with any scraper you build.

## Installation

### Option 1: Install with pip

```bash
pip install scraper-spec
```

### Option 2: Install with uv (Recommended)

```bash
# Install globally as a tool
uv tool install git+https://github.com/rainbowgore/scraping-spec-kit.git

# Or run directly without installing
uvx --from git+https://github.com/rainbowgore/scraping-spec-kit.git scraper-spec --help
```

## Quick Start

```bash
# Initialize framework in your project
cd your-scraping-project
scraper-spec setup

# Create a site spec
scraper-spec init example-site

# Edit specs/example-site.yaml with your selectors

# Create baseline
scraper-spec baseline example-site "test query"

# Test for regressions
scraper-spec test example-site

# Release stable version
scraper-spec release example-site
```

## Available Commands

### Setup & Initialization

- `scraper-spec setup` - Initialize framework structure in current directory
- `scraper-spec check` - Check environment and framework setup
- `scraper-spec init <site-name>` - Create a new site specification file

### Development & Testing

- `scraper-spec discover <site-name>` - Start site discovery (creates `specs/<site>.discover.yaml` with candidates)
- `scraper-spec baseline <site-name> "<query>"` - Create baseline artifacts
- `scraper-spec test <site-name>` - Run regression test against baseline
- `scraper-spec debug <site-name> "<query>"` - Generate debug artifacts

### Version Control

- `scraper-spec release <site-name>` - Tag stable version and update changelog
- `scraper-spec rollback <site-name>` - Restore last stable spec and baseline
- `scraper-spec rebaseline <site-name> "<query>"` - Promote debug run to baseline

### MCP Integration (Stubs)

- `scraper-spec push <site-name>` - Push spec to MCP context
- `scraper-spec pull <site-name>` - Pull spec from MCP context

## How It Works

The framework enforces a strict spec lifecycle through multiple enforcement mechanisms:

### 1. Setup Gate

- **Only `setup` and `check` commands work** before `.scraper-spec/` exists
- All other commands hard-fail with clear error: "Run: scraper-spec setup"
- This ensures proper initialization before any work begins

### 2. Path Rules (Constitution Compliance)

- **All file writes must be** in allowed directories: `specs/`, `baselines/`, `logs/`, `docs/`, `framework/`
- Commands abort with specific error if path violates rules
- Example: `"ERROR: Output path X violates constitution (top-level 'bad-dir' not allowed)"`

### 3. Schema Validation

- **All JSON/YAML artifacts are validated** against templates on write:
  - `specs/*.yaml` → validated against `selectors-template.yaml`
  - `baselines/*.json` → validated against `baseline-template.json`
  - `logs/*.json` (runtime and debug) → validated against `log-template.json` / `debug-log-template.json`
  - Diffs → validated against `diff-template.json`
- HTML snapshots are advisory and not schema-validated
- If validation fails, command aborts with error

### 4. Critical Path Enforcement

- **Plans must include all phases** defined in `.scraper-spec/config.yaml`
- Default abstract phases: `Acquire → Identify → Collect → Extract`
- Both presence AND order are validated
- Configurable for different scraping approaches (web, API, feed, file)

### 5. Versioning & Release Guards

- `release` command bumps spec version and updates changelog
- `baseline` command blocks if baseline exists (requires `SCRAPER_SPEC_CONFIRM=1` or use `rebaseline`)
- This prevents accidental overwrites of golden data

### 6. Regression Testing Loop

- `baseline` creates golden artifacts (expected.json, snapshot.html, screenshots, log.json)
- `test` compares current outputs to baseline and logs diffs
- Structured diff files show exactly what changed

### 7. Artifact Completeness Checks

- After `baseline`: framework verifies `expected.json`, `snapshot.html`, `screenshot.png`, and `log.json` exist; aborts if any missing
- After `test`: framework verifies the diff JSON exists; aborts if missing

**Result**: Every project follows the same reproducible loop:

```
setup → check → init → edit spec → baseline → test → release
```

This is why we call it a **spec lifecycle enforcer**, not a scraper library.

## Framework Structure

After running `scraper-spec setup`, you'll have:

```
your-project/
├── .scraper-spec/           # Framework templates and constitution
│   ├── commands/            # Command documentation
│   ├── memory/              # Constitutional rules
│   └── templates/           # File templates
├── specs/                   # Site specifications (.yaml files)
│   └── SCRAPER_SPEC.md     # Framework charter
├── baselines/               # Baseline artifacts
│   └── screenshots/         # Visual baselines
├── logs/                    # Execution logs
│   ├── debug/              # Debug artifacts
│   └── regressions/        # Test results
├── docs/                    # Documentation
│   └── CHANGELOG.md        # Version history
└── framework/               # Your scraper implementation
    └── plan.md             # Development plan
```

## Workflow

### 1. Discover Phase

Explore the target site and identify selectors:

```bash
scraper-spec discover example-site
```

### 2. Specify Phase

Edit the generated spec file with your selectors:

```yaml
# specs/example-site.yaml
site_config:
  base_url: "https://example.com"

selectors:
  search_box: "#search"
  results_list: ".results"
  result_item: ".result-item"
```

### 3. Baseline Phase

Create baseline artifacts with a test query:

```bash
scraper-spec baseline example-site "test query"
```

### 4. Test Phase

Run regression tests to detect changes:

```bash
scraper-spec test example-site
```

### 5. Release Phase

Lock stable versions:

```bash
scraper-spec release example-site
```

## Development

### Prerequisites

- Python 3.8+
- pip

### Installing from Source

```bash
git clone https://github.com/rainbowgore/scraping-spec-kit.git
cd scraping-spec-kit
pip install -e .
```

### Running Tests

```bash
python -m pytest tests/
```

## Requirements

- `jsonschema>=4.0.0` - For validating JSON artifacts
- `PyYAML>=6.0` - For parsing YAML specifications

## Use Cases

### Automation Engineers

- Standardize scraper configurations across projects
- Detect breaking changes in target sites
- Maintain audit trails for compliance
- Enforce coding standards via constitutional rules

### Quality Assurance

- Visual regression testing with screenshots
- Automated baseline comparison
- Historical tracking of site changes

### Team Collaboration

- Shared specification format
- Version-controlled baselines
- Clear documentation of selectors and expectations

## Constitutional Rules

The framework enforces rules defined in `.scraper-spec/memory/constitution.md`:

- Allowed top-level directories: `specs/`, `baselines/`, `logs/`, `docs/`, `framework/`
- All artifacts must comply with templates
- Version control is enforced for releases
- Critical path phases must be preserved in all plans (configurable in `.scraper-spec/config.yaml`)

### Critical Path Enforcement

The framework validates that all implementation plans follow a defined critical path. By default, the abstract phases are:

1. **Acquire** - Connect to data source (web page, API, feed, file)
2. **Identify** - Locate target elements or endpoints
3. **Collect** - Gather the raw data
4. **Extract** - Transform raw data into structured output

These phases are tool-agnostic and work for any scraping approach (browser automation, API crawling, feed parsing, etc.).

**Customization**: Edit `.scraper-spec/config.yaml` to define your own phases:

```yaml
critical_path:
  phases:
    - Connect
    - Discover
    - Retrieve
    - Transform
    - Validate
```

## Advanced Features

### Debug Mode

Generate detailed debug artifacts:

```bash
scraper-spec debug example-site "test query"
```

### Rollback

Restore previous stable versions:

```bash
scraper-spec rollback example-site
```

### Rebaseline

Promote a successful debug run to baseline:

```bash
SCRAPER_SPEC_CONFIRM=1 scraper-spec rebaseline example-site "test query"
```

## Troubleshooting

### Framework not initialized errors

**Problem**: `ERROR: Framework not initialized in this directory`

**Solution**: Run `scraper-spec setup` to initialize the framework structure.

### Template loading warnings during setup

**Problem**: See "Error loading template" warnings when running `setup`

**Solution**: These are harmless. The validator tries to load templates before they're copied. The setup will complete successfully.

### Path violation errors

**Problem**: `ERROR: Output path X violates constitution (top-level 'Y' not allowed)`

**Solution**: Ensure your output path starts with one of the allowed directories:

- `specs/` - for site specifications
- `baselines/` - for golden artifacts
- `logs/` - for execution logs
- `docs/` - for documentation
- `framework/` - for implementation

### Baseline already exists

**Problem**: `ERROR: Baseline exists at baselines/<site>.expected.json`

**Solution**:

- Use `scraper-spec rebaseline <site> "<query>"` to promote a debug run, OR
- Set `SCRAPER_SPEC_CONFIRM=1` environment variable to force overwrite

### Missing templates after installation

**Problem**: Commands fail with template not found errors

**Solution**:

1. Reinstall the package: `pip install --force-reinstall scraper-spec`
2. Re-run `scraper-spec setup` in your project

### Critical path validation failures

**Problem**: `ERROR: Plan violates constitution (phase 'X' missing from critical path)`

**Solution**: Ensure your `framework/plan.md` includes all phases from `.scraper-spec/config.yaml` in order.
Default phases: Acquire → Identify → Collect → Extract

### Empty logs/ directory

**Note**: The `logs/` directory is empty until you run commands. Logs populate after:

- `baseline` → creates `logs/<site>_<timestamp>.log.json`
- `test` → creates `logs/regressions/<site>_<query>.diff.json`
- `debug` → creates files in `logs/debug/`

## Documentation

- [Framework Charter](./specs/SCRAPER_SPEC.md) - After running `setup`
- [Command Reference](./.scraper-spec/commands/) - After running `setup`
- [Constitutional Rules](./.scraper-spec/memory/constitution.md) - After running `setup`
- [Critical Path Guide](./docs/CRITICAL_PATH.md) - Detailed critical path documentation

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

- Issues: https://github.com/rainbowgore/scraping-spec-kit/issues
- Documentation: https://github.com/rainbowgore/scraping-spec-kit/blob/main/README.md

## Acknowledgments

Built for automation engineers who need standardized, testable scraper specifications.
