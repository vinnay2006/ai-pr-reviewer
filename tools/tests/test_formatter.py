def format_test_results(test_results):

    if not test_results:
        return "No test results available."

    # Handle old string format gracefully
    if isinstance(test_results, str):
        return test_results

    passed = test_results.get("passed", 0)
    failed = test_results.get("failed", 0)
    errors = test_results.get("errors", [])

    lines = []
    lines.append(f"Tests: {passed} passed, {failed} failed")

    if not errors:
        lines.append("All tests passed.")
        return "\n".join(lines)

    lines.append("\nFailed Tests:")

    for err in errors:
        lines.append(
            f"  - {err['file']} :: {err['test']}"
            f"\n    Reason: {err['reason']}"
        )

    return "\n".join(lines)