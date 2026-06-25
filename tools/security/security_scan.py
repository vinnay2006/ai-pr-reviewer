import subprocess
import json


def run_security_scan(path="."):

    try:
        result = subprocess.run(
            ["bandit", "-r", path, "-f", "json", "-q"],
            capture_output=True,
            text=True
        )

        raw = result.stdout.strip()

        if not raw:
            return []

        parsed = json.loads(raw)

        results = parsed.get("results", [])

        issues = []

        for item in results:

            severity = normalize_severity(item.get("issue_severity", "LOW"))
            confidence = item.get("issue_confidence", "LOW").lower()

            # Skip low confidence low severity — too noisy
            if severity == "low" and confidence == "low":
                continue

            issues.append({
                "file": item.get("filename", "unknown"),
                "line": item.get("line_number", 1),
                "severity": severity,
                "confidence": confidence,
                "rule": item.get("test_id", "unknown"),
                "message": item.get("issue_text", "")
            })

        return issues

    except json.JSONDecodeError as e:
        print("Bandit JSON parse error:", e)
        return []

    except Exception as e:
        print("Security scanner error:", e)
        return []


def normalize_severity(sev):
    sev = str(sev).upper()
    mapping = {
        "HIGH":   "high",
        "MEDIUM": "medium",
        "LOW":    "low"
    }
    return mapping.get(sev, "low")