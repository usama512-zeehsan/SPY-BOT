# bot/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# General bot configuration
SYMBOL = os.getenv("SYMBOL", "SPY")
DAILY_LOSS_LIMIT = float(os.getenv("DAILY_LOSS_LIMIT", -100.0))
TIMEFRAME = os.getenv("TIMEFRAME", "15m")  # For ORB logic (e.g., 15-minute ORB)
