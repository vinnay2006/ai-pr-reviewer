import sys
import os
os.environ["PYTHONUNBUFFERED"] = "1"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import hmac
import hashlib
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from reviewer_agent.graph.graph import graph

load_dotenv()

app = Flask(__name__)

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "")


def verify_signature(payload_body, signature_header):

    if not WEBHOOK_SECRET:
        return True

    if not signature_header:
        return False

    expected = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(),
        payload_body,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected, signature_header)


@app.route("/webhook", methods=["POST"])
def webhook():

    signature = request.headers.get("X-Hub-Signature-256", "")
    if not verify_signature(request.data, signature):
        print("Invalid signature", flush=True)
        return jsonify({"error": "Invalid signature"}), 401

    event = request.headers.get("X-GitHub-Event", "")
    payload = request.get_json()

    if not payload:
        print("No payload received", flush=True)
        return jsonify({"error": "No payload"}), 400

    if event != "pull_request":
        print(f"Ignored event: {event}", flush=True)
        return jsonify({"status": "ignored", "event": event}), 200

    action = payload.get("action", "")

    if action not in ["opened", "synchronize"]:
        print(f"Ignored action: {action}", flush=True)
        return jsonify({"status": "ignored", "action": action}), 200

    pr = payload.get("pull_request", {})
    repo = payload.get("repository", {})

    owner = repo.get("owner", {}).get("login", "")
    repo_name = repo.get("name", "")
    pr_number = pr.get("number", 0)

    print(f"\n=== WEBHOOK TRIGGERED ===", flush=True)
    print(f"Event: {event} / {action}", flush=True)
    print(f"PR: {owner}/{repo_name}#{pr_number}", flush=True)

    try:
        result = graph.invoke({
            "owner": owner,
            "repo": repo_name,
            "pr_number": pr_number,
            "diff": "",
            "commit_sha": "",
            "issues": [],
            "review_comments": [],
            "line_map": {},
            "approved": False,
            "logs": []
        })

        logs = result.get("logs", [])
        issues_found = len(result.get("issues", []))

        print(f"Pipeline complete. Issues found: {issues_found}", flush=True)
        print(f"Logs: {logs}", flush=True)

        return jsonify({
            "status": "reviewed",
            "pr": f"{owner}/{repo_name}#{pr_number}",
            "issues_found": issues_found,
            "logs": logs
        }), 200

    except Exception as e:
        print(f"Pipeline error: {e}", flush=True)
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"Webhook server starting on port {port}", flush=True)
    app.run(host="0.0.0.0", port=port, debug=False)