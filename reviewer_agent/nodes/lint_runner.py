from tools.lint.eslint_runner import run_eslint

def lint_runner(state):

    files = state["files_changed"]

    lint_output = run_eslint()

    return {
        "lint_results": lint_output
    }