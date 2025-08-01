# utils/stop_loss.py

from utils.trade import is_loss_limit_hit, get_daily_pnl
from utils.notify import send_telegram_message
from utils.logger import setup_logger

logger = setup_logger("stop_loss")

def enforce_daily_stop():
    if is_loss_limit_hit():
        msg = f"🚫 *STOP TRADING*: Daily loss limit reached (${get_daily_pnl():.2f})"
        logger.warning(msg)
        send_telegram_message(msg)
        return True
    return False
