# # data/quote.py

import requests, os
import pandas as pd
from utils.config import TRADIER_ACCESS_TOKEN, TRADIER_BASE_URL, SYMBOL
from utils.logger import setup_logger

TRADIER_BASE_URL = os.getenv("TRADIER_BASE_URL")
TRADIER_ACCESS_TOKEN = os.getenv("TRADIER_ACCESS_TOKEN")
TRADIER_ACCOUNT_ID = os.getenv("TRADIER_ACCOUNT_ID")

logger = setup_logger("quote")


def get_daily_data(start=None, end=None):
    url = f"{TRADIER_BASE_URL}/markets/history"
    params = {
        "symbol": SYMBOL,
        "interval": "daily",
        "start": start,
        "end": end,
        "session_filter": "all"
    }
    headers = {
        "Authorization": f"Bearer {TRADIER_ACCESS_TOKEN}",
        "Accept": "application/json"
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        raw = res.json()
        candles = raw.get("history", {}).get("day", [])
        df = pd.DataFrame(candles)
        df["datetime"] = pd.to_datetime(df["date"])
        df.set_index("datetime", inplace=True)
        return df
    except Exception as e:
        logger.error(f"Error fetching daily data: {e}")
        return pd.DataFrame()


def get_intraday_data(interval="5min", start=None, end=None):
    url = f"{TRADIER_BASE_URL}/markets/timesales"
    params = {
        "symbol": SYMBOL,
        "interval": interval,
        "start": start,
        "end": end,
        "session_filter": "all"
    }
    headers = {
        "Authorization": f"Bearer {TRADIER_ACCESS_TOKEN}",
        "Accept": "application/json"
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        raw = res.json()
        print(res.json())

        if not raw or "series" not in raw or raw["series"] is None:
            logger.warning(f"No 'series' data in response: {raw}")
            return pd.DataFrame()

        candles = raw["series"].get("data", [])
        if not candles:
            logger.warning("No intraday candle data available.")
            return pd.DataFrame()

        df = pd.DataFrame(candles)
        df["datetime"] = pd.to_datetime(df["timestamp"])
        df.set_index("datetime", inplace=True)
        return df

    except Exception as e:
        logger.error(f"Error fetching intraday data: {e}")
        return pd.DataFrame()

