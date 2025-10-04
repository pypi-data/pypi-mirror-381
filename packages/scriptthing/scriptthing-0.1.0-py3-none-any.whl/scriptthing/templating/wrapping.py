import os
from pathlib import Path
from typing import Dict, Any, List
from jinja2 import Environment, FileSystemLoader
from .paths import list_scripts, get_script_by_name
from ..repo import ensure_default_repo
from ..compiler.analyzers.manager import analyze_script


def _prepare_script_data(script: Path, analysis: Dict[str, Any]) -> Dict[str, Any]:
    """Prepare script data for template rendering."""
    binding_name = script.name.replace("-", "_").replace(".", "_")
    
    # Get argparse data (if available)
    argparse_data = analysis.get('argparse', {})
    
    # Get output format data (if available)
    output_format = analysis.get('output_format')
    if output_format and 'format' in output_format:
        # Add return type mapping based on format
        format_to_type = {
            'json': 'Dict[str, Any]',
            'jsonl': 'List[Dict[str, Any]]',
            'text': 'str',
            'lines': 'List[str]',
            'int': 'int',
            'float': 'float',
            'bool': 'bool'
        }
        output_format['return_type'] = format_to_type.get(output_format['format'], 'Any')
    
    return {
        'name': script.name,
        'binding_name': binding_name,
        'metadata': argparse_data,
        'output_format': output_format,
    }


def generate_all_script_bindings():
    """Generate Python bindings for all discoverable scripts."""
    scripts = list_scripts()
    script_data = []
    
    for script in scripts:
        analysis = analyze_script(script)
        script_info = _prepare_script_data(script, analysis)
        script_data.append(script_info)
    
    # Setup Jinja environment
    template_dir = Path(__file__).parent.parent / 'templates'
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('bindings_module.jinja2')
    
    # Generate bindings
    bindings_content = template.render(scripts=script_data)
    
    # Write to bindings file inside the default repo modules area
    repo = ensure_default_repo()
    modules_dir = repo.root / 'modules'
    modules_dir.mkdir(exist_ok=True)
    bindings_path = modules_dir / 'bindings.py'
    with open(bindings_path, 'w') as f:
        f.write(bindings_content)
