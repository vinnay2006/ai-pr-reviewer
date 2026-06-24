import subprocess

def run_security_scan():
    try:
        result = subprocess.run(
            ["bandit", "-r", "."],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return str(e)