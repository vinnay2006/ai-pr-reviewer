from tools.security.security_scan import run_security_scan
from tools.security.security_formatter import format_security_results


def security_runner(state):

    issues = run_security_scan()

    formatted = format_security_results(issues)

    print("=== SECURITY RESULTS ===")
    print(formatted)

    return {
        "security_results": formatted
    }