import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def get_crypto_markets(per_page, page):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page
    }

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": os.getenv("COINGECKO_API_KEY")
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # raises an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching crypto data: {e}")
        return {"error": str(e)}