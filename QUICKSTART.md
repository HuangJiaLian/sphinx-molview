# Quick Start Guide

## Installation

From the package directory:
```bash
cd sphinx-molview
pip install -e .
```

Or after publishing to PyPI:
```bash
pip install sphinx-molview
```

## Usage in Your Sphinx Project

### 1. Configure Sphinx

Add to your `conf.py`:
```python
extensions = [
    # ... your other extensions
    'sphinx_molview',
]
```

### 2. Copy Static Files

The package needs to serve its JavaScript file. Make sure your Sphinx project has a `_static` directory.

### 3. Use in Documentation

**Basic usage:**
```markdown
\```{molview} https://example.com/structure.xyz
:caption: My molecule
\```
```

**With options:**
```markdown
\```{molview} structure.xyz
:caption: Crystal structure
:height: 600px
:showhbonds: true
:hbondcutoff: 3.2
:extendx: 0.3
:extendy: 0.3
\```
```

**Side-by-side comparison:**
```markdown
\```{molview} before.xyz after.xyz
:caption: Before | After
:showhbonds: true
\```
```

## Testing

Build your documentation:
```bash
cd your-sphinx-project
make html
```

Open `_build/html/index.html` in a browser to see the interactive 3D viewers.

## Moving to Separate Repository

When ready to make this a standalone repository:

```bash
# From the hydrate-structure-discovery root
cd ..
mv hydrate-structure-discovery/sphinx-molview ./sphinx-molview
cd sphinx-molview

# Initialize git
git init
git add .
git commit -m "Initial commit: sphinx-molview molecular visualization extension"

# Create GitHub repository and push
git remote add origin https://github.com/yourusername/sphinx-molview.git
git branch -M main
git push -u origin main
```

## Publishing to PyPI (Optional)

After creating the separate repository:

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Upload to PyPI (requires account)
twine upload dist/*
```

## Development

For development, install in editable mode:
```bash
pip install -e .
```

Changes to Python code will be reflected immediately. For JavaScript changes, rebuild your Sphinx documentation.
