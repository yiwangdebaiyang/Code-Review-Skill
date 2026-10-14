"""Combine deterministic checks into a Markdown report."""
from core.analyzer import analyze
from core.bug_detector import find_warnings
from core.comment_generator import comment_suggestions
from core.code_summary import summarize


def review_code(source: str) -> str:
    tree, overview = analyze(source)
    report = ["# Python Code Review", "", "## Structure", *["- " + line for line in overview]]
    if tree is None:
        report += ["", "Analysis stopped because the source has a syntax error."]
        return "\n".join(report)
    warnings = find_warnings(tree)
    suggestions = comment_suggestions(tree)
    report += ["", "## Possible issues (static checks only)"]
    report += ["- " + issue for issue in warnings] or ["- None detected by these limited rules"]
    report += ["", "## Documentation suggestions"]
    report += ["- " + suggestion for suggestion in suggestions] or ["- All functions have docstrings"]
    report += ["", "## Structure summary", summarize(tree), "", "This tool does not execute the analyzed code or use a language model."]
    return "\n".join(report)
