# indicators/vwap.py

def calculate_vwap(df):
    df["typical_price"] = (df["high"] + df["low"] + df["close"]) / 3
    df["cum_typical_x_volume"] = (df["typical_price"] * df["volume"]).cumsum()
    df["cum_volume"] = df["volume"].cumsum()
    df["vwap"] = df["cum_typical_x_volume"] / df["cum_volume"]
    return df["vwap"]
