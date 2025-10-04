"""Argparse analyzer for Python scripts."""
import ast
from .context import AnalysisContext

def analyze_argparse(context: AnalysisContext) -> None:
    """Extract argparse parameter information from Python scripts and update context."""
    content = context.content
    
    # Quick check if script uses argparse
    if 'argparse' not in content:
        context.set_nested('argparse.has_parser', False)
        context.set_nested('argparse.has_typed_interface', False)
        return
    
    try:
        tree = ast.parse(content)
        
        # Find ArgumentParser creation and add_argument calls
        parser_args = []
        parser_description = ""
        
        class ArgparseVisitor(ast.NodeVisitor):
            def __init__(self):
                self.in_argparse = False
                self.parser_vars = set()
                
            def visit_Call(self, node):
                # Check for ArgumentParser()
                if (isinstance(node.func, ast.Attribute) and 
                    node.func.attr == 'ArgumentParser' and
                    isinstance(node.func.value, ast.Name) and
                    node.func.value.id == 'argparse'):
                    self.in_argparse = True
                    # Extract description from ArgumentParser
                    nonlocal parser_description
                    for keyword in node.keywords:
                        if keyword.arg == 'description':
                            if isinstance(keyword.value, ast.Str):
                                parser_description = keyword.value.s
                            elif isinstance(keyword.value, ast.Constant):
                                parser_description = str(keyword.value.value)
                
                # Check for parser.add_argument()
                elif (isinstance(node.func, ast.Attribute) and 
                      node.func.attr == 'add_argument'):
                    arg_info = self._extract_argument_info(node)
                    if arg_info:
                        parser_args.append(arg_info)
                        
                self.generic_visit(node)
                
            def _extract_argument_info(self, node):
                """Extract information from add_argument call."""
                arg_info = {}
                
                # Get positional arguments (argument names)
                if node.args:
                    names = []
                    for arg in node.args:
                        if isinstance(arg, ast.Str):
                            names.append(arg.s)
                        elif isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                            names.append(arg.value)
                    if names:
                        arg_info['names'] = names
                        arg_info['name'] = names[0].lstrip('-')
                
                # Get keyword arguments
                for keyword in node.keywords:
                    if keyword.arg == 'help':
                        if isinstance(keyword.value, ast.Str):
                            arg_info['help'] = keyword.value.s
                        elif isinstance(keyword.value, ast.Constant):
                            arg_info['help'] = str(keyword.value.value)
                    elif keyword.arg == 'type':
                        if isinstance(keyword.value, ast.Name):
                            arg_info['type'] = keyword.value.id
                    elif keyword.arg == 'default':
                        if isinstance(keyword.value, ast.Constant):
                            arg_info['default'] = keyword.value.value
                        elif isinstance(keyword.value, ast.Str):
                            arg_info['default'] = keyword.value.s
                    elif keyword.arg == 'required':
                        if isinstance(keyword.value, ast.Constant):
                            arg_info['required'] = keyword.value.value
                    elif keyword.arg == 'action':
                        if isinstance(keyword.value, ast.Str):
                            arg_info['action'] = keyword.value.s
                        elif isinstance(keyword.value, ast.Constant):
                            arg_info['action'] = str(keyword.value.value)
                    elif keyword.arg == 'choices':
                        if isinstance(keyword.value, ast.List):
                            choices = []
                            for elt in keyword.value.elts:
                                if isinstance(elt, ast.Str):
                                    choices.append(elt.s)
                                elif isinstance(elt, ast.Constant):
                                    choices.append(str(elt.value))
                            arg_info['choices'] = choices
                
                return arg_info if arg_info else None
        
        visitor = ArgparseVisitor()
        visitor.visit(tree)
        
        if parser_args:
            # Categorize arguments
            positional_args = [arg for arg in parser_args if arg.get('names', [''])[0] and not arg['names'][0].startswith('-')]
            optional_args = [arg for arg in parser_args if arg.get('names', [''])[0] and arg['names'][0].startswith('-')]
            
            # Format for bindings generation
            bindings_positional = []
            bindings_optional = []
            
            # Process positional arguments
            for arg in positional_args:
                bindings_positional.append({
                    'name': arg['name'].replace('-', '_'),
                    'type': _convert_type_for_bindings(arg.get('type'), arg.get('action')),
                    'help': arg.get('help', '')
                })
            
            # Process optional arguments  
            for arg in optional_args:
                # Determine default value
                default = arg.get('default')
                if arg.get('action') == 'store_true':
                    default = False
                elif arg.get('action') == 'store_false':
                    default = True
                
                # Get command line flag (prefer long form)
                flag = None
                for name in arg.get('names', []):
                    if name.startswith('--'):
                        flag = name
                        break
                if not flag and arg.get('names'):
                    flag = arg['names'][0]
                
                bindings_optional.append({
                    'name': arg['name'].replace('-', '_'),
                    'type': _convert_type_for_bindings(arg.get('type'), arg.get('action')),
                    'default': default,
                    'flag': flag,
                    'help': arg.get('help', '')
                })
            
            # Update context with argparse metadata
            context.set_nested('argparse.has_parser', True)
            context.set_nested('argparse.has_typed_interface', True)
            context.set_nested('argparse.description', parser_description)
            context.set_nested('argparse.positional', bindings_positional)
            context.set_nested('argparse.optional', bindings_optional)
        else:
            context.set_nested('argparse.has_parser', False)
            context.set_nested('argparse.has_typed_interface', False)
            
    except Exception:
        context.set_nested('argparse.has_parser', False)
        context.set_nested('argparse.has_typed_interface', False)
        context.set_nested('argparse.error', 'Failed to parse')





def _convert_type_for_bindings(arg_type: str, action: str = None) -> str:
    """Convert argparse type to Python type annotation."""
    if action in ('store_true', 'store_false'):
        return 'bool'
    elif arg_type == 'int':
        return 'int'
    elif arg_type == 'float':
        return 'float'
    else:
        return 'str'