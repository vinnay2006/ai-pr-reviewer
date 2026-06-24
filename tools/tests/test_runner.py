import subprocess

def run_tests():
    try:
        result = subprocess.run(
            ["pytest", "-q"],
            capture_output=True,
            text=True
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)