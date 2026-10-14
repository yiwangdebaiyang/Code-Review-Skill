"""Summarize basic Python program structure."""
import ast


def summarize(tree: ast.AST) -> str:
    func_names = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    class_names = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    parts = []
    if class_names:
        parts.append("Defines classes: " + ", ".join(class_names))
    if func_names:
        parts.append("Defines functions: " + ", ".join(func_names))
    if not parts:
        parts.append("No function or class definitions detected")
    return ". ".join(parts) + "."
