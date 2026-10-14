---
name: python-code-review
description: Review Python source files for syntax errors, risky static patterns, missing function docstrings, and basic code structure. Use when a user asks to check a Python program for bugs, explain its functions, summarize its code structure, or improve comments; run the bundled app.py for deterministic checks and clearly distinguish findings from unverified guesses.
---

# Python Code Review

1. Ask the user for the `.py` source file or use a Python file they provided.
2. Review the code without executing the submitted source. If local execution is available, run `python app.py path/to/file.py` from this skill directory. Use `--output report.md` only when a saved Markdown report is requested.
3. Report syntax errors first. If parsing fails, do not claim to have inspected deeper semantics.
4. Explain the structure, functions, and expected behavior using the source, not just static counts. Suggest clear function docstrings, meaningful names, and test cases.
5. Classify findings: confirmed syntax error, rule-based warning, and possible logic issue requiring tests. Do not call a rule-based warning a proven bug.
6. Provide a concise Markdown report with sections: Overview, Syntax, Potential Issues, Comment Suggestions, Code Summary, and Suggested Tests.
7. Do not execute untrusted user code. Never request or reveal secrets or credentials.

The bundled helper uses only Python's standard library and does not access an LLM API. See `README.md` for local running instructions.
