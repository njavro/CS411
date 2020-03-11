from newsapi.newsapi_client import NewsApiClient
# Init
newsapi = NewsApiClient(api_key='0001bb0b99014f8ba9a07902822c819e')


class NewsObject(object):
	"""docstring for NewsObject"""
	def __init__(self, given_title, given_description, given_url):
		self.title = given_title
		self.description = given_description
		self.url = given_url

		

class NewsListObject(object):
	"""docstring for NewsListObject"""
	def __init__(self, companyName, object_size=5):
		self.objectSize = object_size
		self.companyName = companyName

		# /v2/Everythingn latest come first
		self.new_headlines = newsapi.get_everything(q=companyName,language='en',sort_by='publishedAt')
		self.news_list = []


		#Populate news_list
		if object_size > self.new_headlines['totalResults']:
			for i in range(self.new_headlines['totalResults']):
				new_news_object = NewsObject(self.new_headlines['articles'][i]['title'],self.new_headlines['articles'][i]['description'],self.new_headlines['articles'][i]['url'])
				self.news_list.append(new_news_object)
		else:
			for i in range(object_size):
				new_news_object = NewsObject(self.new_headlines['articles'][i]['title'],self.new_headlines['articles'][i]['description'],self.new_headlines['articles'][i]['url'])
				self.news_list.append(new_news_object)


	def show_news_list(self):
		#Used For Testing purposes
		for x in self.news_list:
			print(x.title)


#To Test: Works!
#my_news_list = NewsListObject("MSFT",3)
#my_news_list.show_news_list()