import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

GUMROAD_API_KEY = os.environ.get("GUMROAD_API_KEY")
if not GUMROAD_API_KEY:
    # For safety, the server will still start but will return an error until the env var is set.
    app.logger.warning("GUMROAD_API_KEY not set. License verification will not work until configured.")

GUMROAD_VERIFY_URL = "https://api.gumroad.com/v2/licenses/verify"

@app.route("/verify", methods=["POST"])
def verify_license():
    data = request.get_json(force=True)
    license_key = data.get("license_key")
    product_id = data.get("product_id")

    if not license_key:
        return jsonify({"valid": False, "message": "Missing license_key"}), 400

    if not GUMROAD_API_KEY:
        return jsonify({"valid": False, "message": "Server not configured with GUMROAD_API_KEY."}), 500

    try:
        # Gumroad's verify endpoint expects form-encoded data. We include the product permalink (product_id)
        resp = requests.post(
            GUMROAD_VERIFY_URL,
            data={"product_permalink": product_id, "license_key": license_key},
            headers={"Authorization": f"Bearer {GUMROAD_API_KEY}"},
            timeout=10,
        )
        resp.raise_for_status()
        result = resp.json()
        # The structure depends on Gumroad's response. We handle the expected shape.
        if result.get("success") and result.get("purchase"):
            return jsonify({"valid": True, "purchase": result.get("purchase")})
        else:
            return jsonify({"valid": False, "message": result.get("message", "Invalid license")}), 200
    except requests.RequestException as e:
        app.logger.exception("Error verifying license with Gumroad")
        return jsonify({"valid": False, "message": str(e)}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
