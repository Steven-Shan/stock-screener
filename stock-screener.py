import yfinance as yf
import csv as csv
from datetime import date

def check_stock_criteria(ticker):
    stock_characteristics = []
    stock_characteristics.append(ticker)
    
    stock = yf.Ticker(ticker)
    print(ticker)
    info = stock.info
    
    name = info.get('shortName')
    stock_characteristics.append(name)
    # Extracting financial metrics
    peg_ratio = info.get('pegRatio')
    stock_characteristics.append(peg_ratio)
    market_cap = info.get('marketCap')
    stock_characteristics.append(market_cap)
    # Derived variable: price to cash flow
    fcf = info.get('freeCashflow')
    stock_characteristics.append(fcf)
    shares = info.get('sharesOutstanding')
    stock_characteristics.append(shares)
    price = info.get('currentPrice')
    stock_characteristics.append(price)
    print(price)
    price_to_cashflow = None
    if(fcf is not None and shares is not None and price is not None): 
        price_to_cashflow = price/(fcf/shares)
        stock_characteristics.append(price_to_cashflow)
    else:
        stock_characteristics.append("null")
    insiderOwnership = info.get('heldPercentInsiders')
    stock_characteristics.append(insiderOwnership)
    # Check criteria
    #if peg_ratio is not None and peg_ratio < 1:
    #    if price_to_cashflow is not None and price_to_cashflow < 10:
    #        if market_cap is not None and market_cap >= 2000000000:
    #            #return True
    return stock_characteristics

# Example usage
#ticker = "AAPL"  # Replace with the ticker you want to check
#if check_stock_criteria(ticker):
#    print(f"{ticker} meets the criteria.")
#else:
#    print(f"{ticker} does not meet the criteria.")
    
def main():
    headers = ["Ticker", "Name", "pegRatio", "marketCap", "freeCashflow", "sharesOutstanding", "currentPrice", "percentHeldInsiders"]
    # This will be done as a chron/batch job that writes daily
    today = date.today()
    file_name = "Insider Ownership " + str(today)
    with open(file_name, 'w', newline='') as file1:
        writer = csv.writer(file1)
        writer.writerow(headers)
    file1.close()
    
    with open('SP1500 Tickers.csv', mode = 'r', encoding='utf-8-sig') as file:
        csvFile = csv.reader(file)
        
        for lines in csvFile:
            ticker = lines[0]  # Replace with the ticker you want to check
            print(ticker)
            with open(file_name, 'a', newline='') as file1:
                writer = csv.writer(file1)
                writer.writerow(check_stock_criteria(ticker))
                file1.close()
            #if check_stock_criteria(ticker):
               #print(ticker)
    print("Done")
main()
