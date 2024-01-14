import yfinance as yf


def check_stock_criteria(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    # Extracting financial metrics
    peg_ratio = info.get('pegRatio')
    price_to_cashflow = info.get('priceToCashflow')
    market_cap = info.get('marketCap')

    # Check criteria
    if peg_ratio is not None and peg_ratio < 1:
        if price_to_cashflow is not None and price_to_cashflow < 10:
            if market_cap is not None and market_cap >= 2000000000:
                return True

    return False


# Example usage
ticker = "AAPL"  # Replace with the ticker you want to check
if check_stock_criteria(ticker):
    print(f"{ticker} meets the criteria.")
else:
    print(f"{ticker} does not meet the criteria.")
