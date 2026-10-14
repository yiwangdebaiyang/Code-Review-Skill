"""Run: python app.py examples/demo.py"""
import argparse
from pathlib import Path
from core.ai_review import review_code


def main() -> None:
    parser = argparse.ArgumentParser(description="Basic Python code review")
    parser.add_argument("file", help="Path to a Python file to inspect")
    parser.add_argument("--output", help="Optional path to save Markdown report")
    args = parser.parse_args()
    path = Path(args.file)
    if path.suffix.lower() != ".py" or not path.is_file():
        parser.error("Please provide an existing .py file")
    source = path.read_text(encoding="utf-8")
    report = review_code(source)
    print(report)
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"\nSaved report to {args.output}")


if __name__ == "__main__":
    main()
