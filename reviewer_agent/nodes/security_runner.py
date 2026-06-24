from tools.security.security_scan import run_security_scan

def security_runner(state):

    security_output = run_security_scan()

    return {
        "security_results": security_output
    }