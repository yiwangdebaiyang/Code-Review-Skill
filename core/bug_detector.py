"""Basic static warnings, not a proof that code is buggy."""
import ast


def find_warnings(tree: ast.AST) -> list[str]:
    warnings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            if isinstance(node.right, ast.Constant) and node.right.value == 0:
                warnings.append(f"Line {node.lineno}: division or remainder by literal zero")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec"}:
            warnings.append(f"Line {node.lineno}: review use of {node.func.id}() with untrusted input")
        if isinstance(node, ast.ExceptHandler) and node.type is None:
            warnings.append(f"Line {node.lineno}: bare except may hide errors")
    return warnings
