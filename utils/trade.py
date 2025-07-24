import random
from utils.config import DAILY_LOSS_LIMIT

daily_pnl = 0

def place_mock_trade():
    global daily_pnl
    trade_pnl = random.randint(-70, 50)
    daily_pnl += trade_pnl
    return trade_pnl

def is_loss_limit_hit():
    return daily_pnl <= DAILY_LOSS_LIMIT

def get_daily_pnl():
    return daily_pnl
