from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.
def home(request):

	return render(request,'index.html',{})


def main(request):
	import requests
	import json
	from newsapi import NewsApiClient

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/{}/quote?token=pk_67513180ad73424ca6137332a00e6ef8".format(ticker))
		news_api = NewsApiClient(api_key ='0001bb0b99014f8ba9a07902822c819e')
		top_headlines = news_api.get_top_headlines(q=ticker,category='business',language='en',country='us')
		try:
			api = json.loads(api_request.content)
			top_headlines = news_api.get_top_headlines(q=api['companyName'],category='business',language='en',country='us')
		except Exception as e:
			api = "Error..."
		articles = top_headlines['articles']
		news_list = []
		max_len = max(5,len(articles))

		for i in range(len(articles)):
			article = articles[i]
			news_list.append((article['title'],article['source']['name'],article['description'],article['urlToImage']))
		#news_aggregate = zip(news,desc,img)
		
		return render(request,'main.html',{'api': api, 'news_list': news_list})

	else:
		return render(request,'main.html',{'ticker': "Enter a ticket symbol above..."})
	#API KEY: pk_67513180ad73424ca6137332a00e6ef8


def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/{}/quote?token=pk_67513180ad73424ca6137332a00e6ef8".format(str(ticker_item)))
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request,'add_stock.html',{'ticker':ticker, 'output':output})




def stock_news(request):
	import requests
	import json
	from newsapi import NewsApiClient

	if request.method == 'POST':
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('stock_news')
	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/{}/quote?token=pk_67513180ad73424ca6137332a00e6ef8".format(str(ticker_item)))
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request,'stock_news.html',{'ticker':ticker, 'output':output})




def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request,("Stock has been deleted!"))
	return redirect('delete_stock')


def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})
	pass
