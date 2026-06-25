import subprocess
import json


def run_eslint(path="."):

    try:
        result = subprocess.run(
            ["npx", "eslint", path, "--format", "json", "--no-eslintrc", "--env", "es6"],
            capture_output=True,
            text=True
        )

        raw = result.stdout.strip()

        if not raw:
            return []

        parsed = json.loads(raw)

        lint_issues = []

        for file_result in parsed:

            filepath = file_result.get("filePath", "unknown")
            messages = file_result.get("messages", [])

            for msg in messages:

                severity_code = msg.get("severity", 1)
                severity = "error" if severity_code == 2 else "warning"

                lint_issues.append({
                    "file": filepath,
                    "line": msg.get("line", 1),
                    "column": msg.get("column", 1),
                    "severity": severity,
                    "rule": msg.get("ruleId", "unknown"),
                    "message": msg.get("message", "")
                })

        return lint_issues

    except json.JSONDecodeError as e:
        print("ESLint JSON parse error:", e)
        return []

    except Exception as e:
        print("ESLint runner error:", e)
        return []