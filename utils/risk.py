# utils/risk.py
import os

MAX_TRADES_PER_DAY = int(os.getenv("MAX_TRADES_PER_DAY", 5))
MAX_EXPOSURE = float(os.getenv("MAX_EXPOSURE", 1000.0))

trade_counter = 0
exposure = 0

def can_trade(amount):
    global trade_counter, exposure
    if trade_counter >= MAX_TRADES_PER_DAY:
        return False
    if exposure + amount > MAX_EXPOSURE:
        return False
    trade_counter += 1
    exposure += amount
    return True
