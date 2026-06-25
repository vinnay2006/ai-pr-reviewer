import subprocess
import re


def run_tests():

    try:
        result = subprocess.run(
            ["pytest", "-q", "--tb=short", "--no-header"],
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr

        return parse_pytest_output(output)

    except Exception as e:
        return {
            "passed": 0,
            "failed": 0,
            "errors": [],
            "raw": str(e)
        }


def parse_pytest_output(output):

    passed = 0
    failed = 0
    errors = []

    # Extract summary line e.g. "2 failed, 5 passed in 1.23s"
    summary_match = re.search(
        r"(\d+) failed.*?(\d+) passed|(\d+) passed|(\d+) failed",
        output
    )

    if summary_match:
        groups = summary_match.groups()
        if groups[0]:
            failed = int(groups[0])
        if groups[1]:
            passed = int(groups[1])
        elif groups[2]:
            passed = int(groups[2])
        elif groups[3]:
            failed = int(groups[3])

    # Extract individual FAILED lines e.g. "FAILED tests/test_app.py::test_login - AssertionError"
    failed_lines = re.findall(r"FAILED (.+?) - (.+)", output)

    for test_path, reason in failed_lines:
        # Split test_path into file and test name
        parts = test_path.split("::")
        file_path = parts[0] if parts else test_path
        test_name = parts[1] if len(parts) > 1 else test_path

        errors.append({
            "file": file_path,
            "test": test_name,
            "reason": reason.strip()
        })

    # Extract ERROR lines e.g. "ERROR tests/test_app.py - ImportError"
    error_lines = re.findall(r"ERROR (.+?) - (.+)", output)

    for test_path, reason in error_lines:
        parts = test_path.split("::")
        file_path = parts[0] if parts else test_path
        test_name = parts[1] if len(parts) > 1 else test_path

        errors.append({
            "file": file_path,
            "test": test_name,
            "reason": f"ERROR: {reason.strip()}"
        })

    return {
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "raw": output[:300] if errors else "All tests passed."
    }