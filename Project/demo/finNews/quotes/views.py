from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.
def home(request):
	
	return render(request,'index.html',{})


def about(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/{}/quote?token=pk_67513180ad73424ca6137332a00e6ef8".format(ticker))
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request,'about.html',{'api': api})
		
	else:
		return render(request,'about.html',{'ticker': "Enter a ticket symbol above..."})
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





def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()

	messages.success(request,("Stock has been deleted!"))
	return redirect(add_stock)