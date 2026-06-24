import subprocess

def run_eslint(path="."):
    try:
        result = subprocess.run(
            ["npx", "eslint", path, "-f", "json"],
            capture_output=True,
            text=True
        )

        return result.stdout
    except Exception as e:
        return str(e)