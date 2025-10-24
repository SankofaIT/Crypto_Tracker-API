# routes/crypto_routes.py
from flask import Blueprint, jsonify
import requests
from services.crypto_services import get_crypto_markets

# --- Create the Blueprint ---
# "crypto" = internal Flask name for this module (like a department name)
# __name__ = lets Flask know where this file lives
crypto_bp = Blueprint("crypto", __name__)

#Incoporate a highlight feataure#
#Research different Crypto Portfolio trackers and compare/contrast. Implement them#
#Look into some Crypto Research#

# --- Example route: fetch crypto market data ---
@crypto_bp.route("/markets", methods=["GET"])
def get_markets():
    """
    Fetches a list of cryptocurrency market data from a public API (CoinGecko)
    and returns it as JSON to the client.
    """
    try:
        # Dynamically read URL parameters (e.g. ?per_page=50&page=2)
        per_page = requests.args.get("per_page", default=10, type=int)
        page = requests.args.get("page", default=1, type=int)

        data = get_crypto_markets(per_page=per_page, page=page)
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- Another example route: get details for a specific coin ---
@crypto_bp.route("/coin/<coin_id>", methods=["GET"])
def get_coin_details(coin_id):
    """
    Fetches detailed data for a specific cryptocurrency by its ID.
    For example: /api/crypto/coin/bitcoin
    """
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}")
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500