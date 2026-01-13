# Journeyman Electrician Exam Prep (fix/streamlit-license)

This branch adds a cleaned Streamlit app and a minimal Flask license-verification example to help you sell the app securely via Gumroad.

What I added:
- app.py — fixed Streamlit application (trial gating, per-question timing, score tracking, optional server-side license verification)
- server/license_verifier/app.py — small Flask example that verifies Gumroad license keys (requires GUMROAD_API_KEY env var)
- requirements.txt — Python dependencies
- .github/workflows/ci.yml — basic CI that checks Python files compile
- .gitignore

Quick start (local):
1. Create a Python venv and activate it:
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
2. Install requirements:
   pip install -r requirements.txt
3. (Optional) Run the license verifier server (in a separate terminal):
   export GUMROAD_API_KEY="your_gumroad_api_key"
   cd server/license_verifier
   python app.py
4. Run the Streamlit app (in repo root):
   export LICENSE_SERVER_URL="http://localhost:5000"  # if running the verifier locally
   streamlit run app.py

Deployment recommendations:
- Streamlit Community Cloud is the easiest for app.py. Configure LICENSE_SERVER_URL in Streamlit secrets if you use the verifier.
- Deploy the Flask verifier to Render, Heroku, or any small server and set GUMROAD_API_KEY in the host's environment variables.

Important security notes:
- Never commit your GUMROAD_API_KEY. Set it in environment variables on your host or GitHub Secrets.
- This example uses a simple verify pattern. For production, secure the verifier (rate-limit, logging, authentication) and consider issuing short-lived tokens to the client.

If you'd like, I can:
- Open a PR with these changes (I already pushed to branch `fix/streamlit-license`).
- Add GitHub Actions deployment steps to deploy the verifier to Render automatically when you push tags.
