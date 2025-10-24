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

    response = requests.get(url, params=params, headers=headers)
    return response.json()