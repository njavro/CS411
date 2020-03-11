import yfinance as yf

msft = yf.download("MSFT", period="1d")
msft.info
#print(msft)
print(msft.iloc(0)[0][1])