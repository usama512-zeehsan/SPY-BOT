import random
import datetime

def get_mock_rsi():
    return random.randint(30, 70)

def has_opening_range_broken():
    current_time = datetime.datetime.now()
    market_open = current_time.replace(hour=9, minute=30, second=0, microsecond=0)
    return (current_time - market_open).total_seconds() >= 15 * 60
