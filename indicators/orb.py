# indicators/orb.py

def calculate_orb_range(df):
    orb_window = df.between_time("09:30", "09:44")
    high = orb_window["high"].max()
    low = orb_window["low"].min()
    return high, low
