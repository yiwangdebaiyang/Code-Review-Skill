"""Parse Python code and describe its structure."""
import ast


def analyze(source: str) -> tuple[ast.AST | None, list[str]]:
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return None, [f"Syntax error at line {exc.lineno}: {exc.msg}"]
    functions = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    loops = [node for node in ast.walk(tree) if isinstance(node, (ast.For, ast.While, ast.AsyncFor))]
    lines = ["Syntax: OK", f"Functions: {len(functions)}", f"Classes: {len(classes)}", f"Loops: {len(loops)}"]
    lines += [f"Function: {item.name} (line {item.lineno})" for item in functions]
    lines += [f"Class: {item.name} (line {item.lineno})" for item in classes]
    return tree, lines
