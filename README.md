# sphinx-molview

A Sphinx extension for interactive 3D molecular visualisation using 3Dmol.js.

![](https://raw.githubusercontent.com/HuangJiaLian/DataBase0/master/uploads/screenshot_251207_010223.png)

## Features

- **Multiple file formats**: XYZ, POSCAR/VASP, CIF, PDB, SDF, MOL2
- **Interactive controls**: Rotate, zoom, view along crystal axes
- **Hydrogen bond visualization**: Automatic H-bond detection and display
- **Atom manipulation**: Select, delete atoms, and save modified structures
- **POSCAR support**: Preserves selective dynamics flags (T/F) when saving
- **Periodic extension**: Extend structures along lattice vectors
- **Side-by-side comparison**: Display two structures simultaneously

## Installation

Install from source:
```bash
pip install git+https://github.com/HuangJiaLian/sphinx-molview.git
```

For local development:
```bash
cd sphinx-molview
pip install -e .
```

## Usage

Add to your Sphinx `conf.py`:
```python
extensions = ['sphinx_molview']
```

In your MyST Markdown files:

```markdown
\```{molview} https://example.com/structure.xyz
:caption: My structure
:extendx: 0.2
:extendy: 0.2
:extendz: 0.2
:showhbonds: true
\```
```

Or in reStructuredText:

```rst
.. molview:: https://example.com/structure.xyz
   :caption: My structure
   :extendx: 0.2
   :extendy: 0.2
   :extendz: 0.2
   :showhbonds: true
```

## Options

- `:caption:` - Caption text to display
- `:height:` - Viewer height (default: "500px")
- `:style:` - Visualisation style: "ball-stick", "stick", "sphere", "line" (default: "ball-stick")
- `:showbox:` - Show unit cell box (default: true)
- `:showcontrols:` - Show control buttons (default: true)
- `:showhbonds:` - Show hydrogen bonds (default: false)
- `:hbondcutoff:` - H-bond distance cutoff in Å (default: 3.5)
- `:extendx:` - Extend structure in X (a) direction (e.g., 0.3 extends 0.3 cells on each side)
- `:extendy:` - Extend structure in Y (b) direction
- `:extendz:` - Extend structure in Z (c) direction
- `:fadeextended:` - Show extended atoms with reduced opacity (default: false)
- `:zoom:` - Zoom level multiplier (default: 1.0, larger values zoom out more)
- `:showborder:` - Show border around canvas (default: true)
- `:view:` - Initial view direction: "c", "c*", "b", "b*", "a", "a*"
- `:format:` - Force file format (auto-detected if not specified)

## Side-by-side viewing

Provide two URLs separated by space:
```markdown
\```{molview} structure1.xyz structure2.xyz
:caption: Structure A | Structure B
\```
```

Use `|` in the caption to split titles for each structure.

## Examples

### Basic XYZ structure
```markdown
\```{molview} my_molecule.xyz
:caption: Water molecule
\```
```

### POSCAR with hydrogen bonds
```markdown
\```{molview} POSCAR
:caption: Ice crystal structure
:showhbonds: true
:hbondcutoff: 3.2
\```
```

### Extended supercell
```markdown
\```{molview} unit_cell.xyz
:caption: 2x2x2 supercell
:extendx: 0.5
:extendy: 0.5
:extendz: 0.5
:fadeextended: true
\```
```

### Compare two structures
```markdown
\```{molview} initial.xyz final.xyz
:caption: Before optimisation | After optimisation
:showhbonds: true
\```
```

### Set initial viewing angle
```markdown
\```{molview} structure.xyz
:caption: View along b-axis
:view: b
:zoom: 1.2
\```
```

Available views: `c`, `c*`, `b`, `b*`, `a`, `a*`

## Interactive Features

- **Rotation**: Click and drag to rotate
- **Zoom**: Scroll to zoom in/out
- **Selection**: Click atoms to select (Shift+click for multiple)
- **Delete**: Select atoms and click the "Delete" button
- **Save**: Export modified structure (preserves format and metadata)
- **View controls**: Buttons to view along crystal axes (a, b, c)

## Requirements

- Python >= 3.8
- Sphinx >= 4.0
- Modern web browser with JavaScript enabled

## License

MIT License

Copyright (c) 2025 Jie Huang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
