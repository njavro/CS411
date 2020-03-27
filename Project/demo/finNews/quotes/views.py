from django.shortcuts import render

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
