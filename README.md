# AI PR Reviewer

An AI-powered GitHub PR reviewer using LangGraph + Gemini.

## Setup

1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt

3. Create a .env file:
   GITHUB_TOKEN=your_github_token
   GOOGLE_API_KEY=your_gemini_key
   WEBHOOK_SECRET=your_webhook_secret

## Run manually

   python main.py

## Run webhook server

   python github/webhook.py

## Expose locally with ngrok (for testing)

   ngrok http 5000

Then register the ngrok URL as a webhook on GitHub:
- Go to your repo → Settings → Webhooks → Add webhook
- Payload URL: https://your-ngrok-url/webhook
- Content type: application/json
- Secret: same as WEBHOOK_SECRET in .env
- Events: Pull requests only

## How it works

1. GitHub sends webhook on PR open/update
2. Flask server receives and verifies the event
3. LangGraph pipeline runs automatically
4. Inline review comments posted to the PR