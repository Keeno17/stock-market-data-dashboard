def calculate_stock_metrics(df):
    close = df["Close"]

    if close.empty:
        raise ValueError("No valid closing prices found.")

    return {
        "avg_price": float(close.mean()),
        "max_price": float(close.max()),
        "min_price": float(close.min()),
        "latest_price": float(close.iloc[-1]),
        "pct_change": float((close.iloc[-1] - close.iloc[0]) / close.iloc[0] * 100)
    }