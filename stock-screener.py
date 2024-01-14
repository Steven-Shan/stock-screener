import yfinance as yf
import csv as csv

def check_stock_criteria(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    # Extracting financial metrics
    peg_ratio = info.get('pegRatio')
    market_cap = info.get('marketCap')

    # Derived variable: price to cash flow
    fcf = info.get('freeCashflow')
    shares = info.get('sharesOutstanding')
    price = info.get('currentPrice')
    price_to_cashflow = price/(fcf/shares)
    
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
    
def main():
    print("Sanity test")
    # Going through the S&P 1500 list (from a State Street ETF)
    with open('SP1500 Tickers.csv', mode = 'r', fileEncoding="UTF-8-BOM") as file:
        csvFile = csv.reader(file)
        
        for lines in csvFile:
            ticker = lines[0]  # Replace with the ticker you want to check
            print(ticker)
            print(check_stock_criteria(ticker))
            #if check_stock_criteria(ticker):
               #print(ticker)
   
    print("Done")
main()
