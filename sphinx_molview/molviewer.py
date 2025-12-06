"""
Custom Sphinx directive for 3D molecular viewer.

Supported formats: xyz, poscar, contcar, vasp, cif, pdb, sdf, mol2

Usage in MyST Markdown:
    ```{molview} https://path/to/file.xyz
    :height: 500px
    :style: ball-stick
    :showbox: true
    :showcontrols: true
    :caption: My Structure
    ```

Or with POSCAR:
    ```{molview} https://path/to/POSCAR
    :format: poscar
    ```

Or minimal:
    ```{molview} https://path/to/file.xyz
    ```

Two structures side-by-side:
    ```{molview} https://path/to/file1.xyz https://path/to/file2.xyz
    :caption: Left Caption | Right Caption
    ```
"""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
import uuid
import os
import shutil


class MolViewDirective(SphinxDirective):
    required_arguments = 1  # URL or local path to xyz file
    optional_arguments = 1  # Optional second URL for side-by-side view
    has_content = False
    option_spec = {
        'height': directives.unchanged,
        'style': directives.unchanged,
        'showbox': directives.unchanged,
        'showcontrols': directives.unchanged,
        'background': directives.unchanged,
        'format': directives.unchanged,
        'caption': directives.unchanged,
        'showhbonds': directives.unchanged,
        'hbondcutoff': directives.unchanged,
        'extendx': directives.unchanged,
        'extendy': directives.unchanged,
        'extendz': directives.unchanged,
        'fadeextended': directives.unchanged,
        'zoom': directives.unchanged,
        'showborder': directives.unchanged,
    }

    def resolve_path(self, path):
        """Resolve a path to a URL, copying local files to _static if needed."""
        if path.startswith('http://') or path.startswith('https://'):
            return path
        
        # Local file - resolve relative to source directory
        src_dir = self.env.srcdir  # doc/ directory
        abs_path = os.path.normpath(os.path.join(src_dir, path))
        
        if os.path.exists(abs_path):
            filename = os.path.basename(abs_path)
            unique_name = f"{uuid.uuid4().hex[:8]}_{filename}"
            static_xyz_dir = os.path.join(src_dir, '_static', 'xyz')
            os.makedirs(static_xyz_dir, exist_ok=True)
            dest_path = os.path.join(static_xyz_dir, unique_name)
            shutil.copy2(abs_path, dest_path)
            return f"_static/xyz/{unique_name}"
        
        return path

    def run(self):
        # Get all file paths
        paths = self.arguments
        urls = [self.resolve_path(p) for p in paths]
        
        # Get options with defaults
        height = self.options.get('height', '500px')
        style = self.options.get('style', 'ball-stick')
        showbox = self.options.get('showbox', 'true').lower() == 'true'
        showcontrols = self.options.get('showcontrols', 'true').lower() == 'true'
        background = self.options.get('background', 'white')
        file_format = self.options.get('format', '')
        caption = self.options.get('caption', '')
        showhbonds = self.options.get('showhbonds', 'false').lower() == 'true'
        hbondcutoff = self.options.get('hbondcutoff', '3.5')
        extendx = self.options.get('extendx', '0')
        extendy = self.options.get('extendy', '0')
        extendz = self.options.get('extendz', '0')
        fadeextended = self.options.get('fadeextended', 'false').lower() == 'true'
        zoom = self.options.get('zoom', '1.0')
        showborder = self.options.get('showborder', 'true').lower() == 'true'

        # Parse captions (split by | for multiple viewers)
        captions = [c.strip() for c in caption.split('|')] if caption else ['', '']
        while len(captions) < len(urls):
            captions.append('')

        # Build options
        format_opt = f", format: '{file_format}'" if file_format else ""
        hbond_opt = f", showHbonds: true, hbondCutoff: {hbondcutoff}" if showhbonds else ""
        extend_opt = f", extendX: {extendx}, extendY: {extendy}, extendZ: {extendz}, fadeExtended: {str(fadeextended).lower()}" if float(extendx) > 0 or float(extendy) > 0 or float(extendz) > 0 else ""
        zoom_opt = f", zoom: {zoom}"
        border_opt = f", showBorder: {str(showborder).lower()}"
        
        if len(urls) == 1:
            # Single viewer
            viewer_id = f"molviewer_{uuid.uuid4().hex[:8]}"
            caption_opt = f", caption: '{captions[0]}'" if captions[0] else ""
            opts = f"height: '{height}', style: '{style}', showBox: {str(showbox).lower()}, showControls: {str(showcontrols).lower()}, background: '{background}'{format_opt}{caption_opt}{hbond_opt}{extend_opt}{zoom_opt}{border_opt}"

            html = f'''
<div id="{viewer_id}"></div>
<script>
createMolViewer("{viewer_id}", "{urls[0]}", {{{opts}}});
</script>
'''
        else:
            # Side-by-side viewers
            viewer_id1 = f"molviewer_{uuid.uuid4().hex[:8]}"
            viewer_id2 = f"molviewer_{uuid.uuid4().hex[:8]}"
            
            caption_opt1 = f", caption: '{captions[0]}'" if captions[0] else ""
            caption_opt2 = f", caption: '{captions[1]}'" if len(captions) > 1 and captions[1] else ""
            
            opts1 = f"height: '{height}', style: '{style}', showBox: {str(showbox).lower()}, showControls: {str(showcontrols).lower()}, background: '{background}'{format_opt}{caption_opt1}{hbond_opt}{extend_opt}{zoom_opt}{border_opt}"
            opts2 = f"height: '{height}', style: '{style}', showBox: {str(showbox).lower()}, showControls: {str(showcontrols).lower()}, background: '{background}'{format_opt}{caption_opt2}{hbond_opt}{extend_opt}{zoom_opt}{border_opt}"

            html = f'''
<div style="display: flex; gap: 10px; width: 100%;">
    <div id="{viewer_id1}" style="flex: 1; min-width: 0;"></div>
    <div id="{viewer_id2}" style="flex: 1; min-width: 0;"></div>
</div>
<script>
createMolViewer("{viewer_id1}", "{urls[0]}", {{{opts1}}});
createMolViewer("{viewer_id2}", "{urls[1]}", {{{opts2}}});
</script>
'''
        raw_node = nodes.raw('', html, format='html')
        return [raw_node]


def setup(app):
    # Register the static directory so mol-viewer.js is copied to _build/_static/
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    app.config.html_static_path.append(static_path)
    
    # Add JavaScript files to HTML head
    app.add_js_file('https://3dmol.org/build/3Dmol-min.js')
    app.add_js_file('mol-viewer.js')
    
    app.add_directive('molview', MolViewDirective)
    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
