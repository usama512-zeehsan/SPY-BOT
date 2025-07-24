import datetime
import time

from utils.rsi import get_mock_rsi, has_opening_range_broken
from utils.trade import place_mock_trade, is_loss_limit_hit, get_daily_pnl

def is_market_open():
    now = datetime.datetime.now(pytz.timezone("US/Eastern"))
    market_open = now.replace(hour=9, minute=30, second=0, microsecond=0)
    market_close = now.replace(hour=16, minute=0, second=0, microsecond=0)
    return market_open <= now <= market_close
    # return True  # <-- Mock it for now 

def run_bot():
    print("📈 Starting SPY 0DTE Bot\n")

    while True:
        # For testing only
        now = datetime.datetime.now().replace(hour=9, minute=30)


        # Exit after market close (assumed 3:00 PM local time)
        if now.hour >= 15:
            print("✅ Market close reached. Stopping bot.")
            break

        # Enforce daily loss limit
        if is_loss_limit_hit():
            print(f"❌ Daily loss limit hit: ${get_daily_pnl()}. Halting trading.")
            break

        # 15-minute Opening Range Breakout logic
        if has_opening_range_broken():
            rsi = get_mock_rsi()
            print(f"📊 RSI Value: {rsi}")

            if 45 <= rsi <= 65:
                pnl = place_mock_trade()
                print(f"✅ Trade executed. PnL: ${pnl}, Daily PnL: ${get_daily_pnl()}")
                # send_telegram_alert(f"Trade placed: PnL ${pnl}, Total: ${get_daily_pnl()}")
            else:
                print("⚠️ RSI outside target range. No trade executed.")
        else:
            print("⏳ Waiting for Opening Range Breakout (15 mins after market open)...")

        time.sleep(60)

if __name__ == "__main__":
    run_bot()
