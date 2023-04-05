import yfinance as yf

# Define the ticker for the stock you want to get data for
ticker = "TSLA", "GOOGL"

# Download 6 months of historical data using the weekly time frame
data = yf.download(ticker, period="6mo", interval="1wk")

# Print the DataFrame to see the data
print(data)
