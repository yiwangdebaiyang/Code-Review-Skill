"""Suggest missing function docstrings without modifying original source."""
import ast


def comment_suggestions(tree: ast.AST) -> list[str]:
    result = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not ast.get_docstring(node):
            result.append(f"Line {node.lineno}: add a docstring for function {node.name}()")
    return result
