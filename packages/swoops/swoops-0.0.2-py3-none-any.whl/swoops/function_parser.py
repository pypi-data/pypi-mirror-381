"""
Written by Jason Krist
06/03/2024

Written with assistance from Github Copilot (using GPT-4.1)
"""

import ast

def flatten_list(lst:list)->list:
    """flatten nested list"""
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def get_returns(node)->dict[str,dict]:
    """
    Given an ast.FunctionDef node, find the variable names used in top-level return statements.
    Returns a list of variable names (or ['expression'] if not a simple variable).
    """
    # Get return annotation as a string, if any
    names = []
    for child in ast.walk(node):
        if isinstance(child, ast.Return):
            value = child.value
            if isinstance(value, ast.Name):
                names.append(value.id)
            elif isinstance(value, ast.Tuple):
                tuple_vars = []
                all_names = True
                for elt in value.elts:
                    if isinstance(elt, ast.Name):
                        tuple_vars.append(elt.id)
                    else:
                        all_names = False
                        break
                if all_names:
                    names.append(tuple_vars)
                else:
                    names.append('expression')
            elif value is not None:
                names.append('expression')
            else:
                names.append(None)
    names = flatten_list(names)
    # Get return annotations
    if node.returns:
        if hasattr(ast, 'unparse'):
            ann_str = ast.unparse(node.returns)
        else:
            ann_str = ast.dump(node.returns)
        # Handles Tuple[int, str], tuple[int, str], (int, str)
        if ann_str.startswith("Tuple[") or ann_str.startswith("tuple["):
            inner = ann_str.split("[", 1)[1].rsplit("]", 1)[0]
            return_annotations = [x.strip() for x in inner.split(",")]
        elif ann_str.startswith("(") and ann_str.endswith(")"):
            inner = ann_str[1:-1]
            return_annotations = [x.strip() for x in inner.split(",")]
        else:
            return_annotations = [ann_str.strip()]
    else:
        return_annotations = None

    # Match return annotations with return names
    returns = {}
    for i,return_name in enumerate(names):
        annotation = None
        if return_annotations:
            annotation = return_annotations[i]
        returns[return_name] = {"name":return_name, "annotation":annotation, "position":i}
    return returns

def get_args(node)->dict[str,dict]:
    args = {}
    pos = 0
    # Positional only (Python 3.8+)
    if hasattr(node.args, "posonlyargs"):
        for arg in node.args.posonlyargs:
            annotation = ast.unparse(arg.annotation) if getattr(arg, "annotation", None) is not None and hasattr(ast, 'unparse') else (ast.dump(arg.annotation) if getattr(arg, "annotation", None) is not None else None)
            args[arg.arg] = {"name":arg.arg, 'annotation': annotation, 'kind': 'positional', 'position':pos}
            pos += 1
    # Regular args (positional or keyword)
    for i, arg in enumerate(node.args.args):
        annotation = ast.unparse(arg.annotation) if getattr(arg, "annotation", None) is not None and hasattr(ast, 'unparse') else (ast.dump(arg.annotation) if getattr(arg, "annotation", None) is not None else None)
        # If there are defaults, last N args are keyword, the rest are positional or positional-or-keyword
        kind = 'positional_or_keyword'
        if node.args.defaults and i >= len(node.args.args) - len(node.args.defaults):
            kind = 'keyword'
        args[arg.arg] = {"name":arg.arg, 'annotation': annotation, 'kind': kind, 'position':pos}
        pos += 1
    # Vararg (*args)
    if node.args.vararg:
        annotation = ast.unparse(node.args.vararg.annotation) if getattr(node.args.vararg, "annotation", None) is not None and hasattr(ast, 'unparse') else (ast.dump(node.args.vararg.annotation) if getattr(node.args.vararg, "annotation", None) is not None else None)
        args[f'*{node.args.vararg.arg}'] = {"name":node.args.vararg.arg, 'annotation': annotation, 'kind': '*args'}
    # Kwonlyargs
    for i, arg in enumerate(node.args.kwonlyargs):
        annotation = ast.unparse(arg.annotation) if getattr(arg, "annotation", None) is not None and hasattr(ast, 'unparse') else (ast.dump(arg.annotation) if getattr(arg, "annotation", None) is not None else None)
        args[arg.arg] = {"name":arg.arg, 'annotation': annotation, 'kind': 'keyword_only'}
    # Kwarg (**kwargs)
    if node.args.kwarg:
        annotation = ast.unparse(node.args.kwarg.annotation) if getattr(node.args.kwarg, "annotation", None) is not None and hasattr(ast, 'unparse') else (ast.dump(node.args.kwarg.annotation) if getattr(node.args.kwarg, "annotation", None) is not None else None)
        args[f'**{node.args.kwarg.arg}'] = {"name":node.args.kwarg.arg, 'annotation': annotation, 'kind': '**kwargs'}
    return args

def parse_functions(file_path:str)->dict[str,dict]:
    """
    Returns a list of dictionaries with function details defined in a Python file.
    Each dictionary contains the function name, its arguments (with type annotations if present),
    and its return annotation (if specified).

    Args:
        file_path (str): Path to the Python file.

    Returns:
        list: List of dictionaries with function details.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    parsed = ast.parse(file_content)
    functions = {}
    for node in ast.walk(parsed):
        if isinstance(node, ast.FunctionDef):
            args = get_args(node)
            returns = get_returns(node)
            functions[node.name] = {
                'name': node.name,
                'args': args,
                'returns': returns,
                #'return_names':return_names,
            }
    return functions
