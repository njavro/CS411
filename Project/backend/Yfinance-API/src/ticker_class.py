import yfinance as yf

class Ticker(object):
	"""docstring for Ticker"""
	def __init__(self, tickerName):
		yfinance_object = yf.download(tickerName, period="1d") #1-day object for latest data
		self.name = tickerName
		self._open = yfinance_object.iloc(0)[0][0] #Open
		self._high = yfinance_object.iloc(0)[0][1] #High
		self._low =  yfinance_object.iloc(0)[0][2] #Low
		self._close = yfinance_object.iloc(0)[0][3] #Close
		self._volume = yfinance_object.iloc(0)[0][5] #Volume


	def (self):