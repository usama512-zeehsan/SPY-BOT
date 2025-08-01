# main.py

import pandas as pd
from datetime import datetime
from data.quote import get_intraday_data, get_daily_data
from indicators.rsi import calculate_rsi
from indicators.vwap import calculate_vwap
from indicators.orb import calculate_orb_range
from utils.config import SYMBOL
from utils.notify import send_telegram_message
from utils.stop_loss import enforce_daily_stop
from utils.trade import place_real_trade
from utils.logger import setup_logger
from dotenv import load_dotenv

load_dotenv()

logger = setup_logger("main")

def fetch_data(interval="5min"):
    today = datetime.now().strftime('%Y-%m-%d')

    if interval in ["1min", "5min", "15min"]:
        return get_intraday_data(interval=interval, start=today, end=today)
    elif interval in ["daily", "weekly", "monthly"]:
        return get_daily_data(start=today, end=today)
    else:
        raise ValueError(f"Invalid interval: {interval}")

def evaluate_signals(df):
    try:
        orb_high, orb_low = calculate_orb_range(df)
        df["rsi"] = calculate_rsi(df["close"])
        df["vwap"] = calculate_vwap(df)
        df["volume_avg"] = df["volume"].rolling(15).mean()
        df["volume_x"] = df["volume"] / df["volume_avg"]

        latest = df.iloc[-1]

        rsi = latest["rsi"]
        volume_x = latest["volume_x"]
        price = latest["close"]
        vwap = latest["vwap"]

        logger.info(f"Price: {price}, RSI: {rsi}, Vol x: {volume_x:.2f}, VWAP: {vwap}, ORB: ({orb_high}, {orb_low})")

        # Check for Bull Put Spread signal
        if price > orb_high and 50 <= rsi <= 65 and volume_x > 1.5 and price > vwap:
            return "bull_put"
        # Check for Bear Call Spread signal
        elif price < orb_low and 35 <= rsi <= 50 and volume_x > 1.5 and price < vwap:
            return "bear_call"
        else:
            return None
    except Exception as e:
        logger.error(f"Signal evaluation failed: {e}")
        return None

def main():
    logger.info("Starting SPY 0DTE Bot...")

    if enforce_daily_stop():
        logger.warning("Stopped due to daily loss limit.")
        return

    df = fetch_data()
    if df.empty or len(df) < 20:
        logger.warning("Not enough data to evaluate.")
        return

    signal = evaluate_signals(df)
    if signal:
        message = f"✅ Signal Detected: *{signal.upper().replace('_', ' ')}* for {SYMBOL}"
        logger.info(message)
        send_telegram_message(message)

        # Simulate order placement (replace with live trade logic if needed)
        place_real_trade(signal, SYMBOL)
    else:
        logger.info("No valid signal yet.")

if __name__ == "__main__":
    main()

