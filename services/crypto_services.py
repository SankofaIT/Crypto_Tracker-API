import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def get_market_data():
    endpoint = f"{BASE_URL}/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()
