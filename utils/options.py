# utils/options.py

import requests, os
from utils.config import TRADIER_BASE_URL, HEADERS

TRADIER_BASE_URL = os.getenv("TRADIER_BASE_URL")
TRADIER_ACCESS_TOKEN = os.getenv("TRADIER_ACCESS_TOKEN")
TRADIER_ACCOUNT_ID = os.getenv("TRADIER_ACCOUNT_ID")

def get_option_chain(symbol, expiry=None, greeks=False):
    url = f"{TRADIER_BASE_URL}/markets/options/chains"
    params = {
        "symbol": symbol,
        "expiration": expiry,
        "greeks": str(greeks).lower()
    }

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        return response.json().get("options", {}).get("option", [])
    else:
        print(f"[OPTIONS ERROR] {response.status_code} - {response.text}")
        return []
