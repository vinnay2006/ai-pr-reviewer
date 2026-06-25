from tools.lint.eslint_runner import run_eslint
from tools.lint.lint_formatter import format_lint_results


def lint_runner(state):

    lint_issues = run_eslint()

    formatted = format_lint_results(lint_issues)

    print("=== LINT RESULTS ===")
    print(formatted)

    return {
        "lint_results": formatted
    }