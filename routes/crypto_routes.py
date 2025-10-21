# routes/crypto_routes.py
from flask import Blueprint, jsonify
import requests

# --- Create the Blueprint ---
# "crypto" = internal Flask name for this module (like a department name)
# __name__ = lets Flask know where this file lives
crypto_bp = Blueprint("crypto", __name__)

# --- Example route: fetch crypto market data ---
@crypto_bp.route("/markets", methods=["GET"])
def get_markets():
    """
    Fetches a list of cryptocurrency market data from a public API (CoinGecko)
    and returns it as JSON to the client.
    """
    try:
        # Call a public API to get data about the top cryptocurrencies
        response = requests.get(
            "https://api.coingecko.com/api/v3/coins/markets",
            params={"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}
        )
        response.raise_for_status()  # Raises an error if something went wrong
        data = response.json()       # Convert response to Python list/dict
        return jsonify(data)         # Flask converts it to JSON for the frontend

    except requests.exceptions.RequestException as e:
        # Handle errors gracefully and return a proper message
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