API_KEY = os.getenv("API_KEY")
print(API_KEY)
url = ('https://newsapi.org/v2/everything?'
       'q=Artsakh&'
       'from=2023-08-03&'
       'sortBy=popularity&'
       f'apiKey={API_KEY}')