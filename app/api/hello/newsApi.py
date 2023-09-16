import requests
import json
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
from keywordFinder import extractKeywords
from imageAPI import getImageURL
import requests
from urllib.parse import urlparse
load_dotenv()

# TODO:
# date changes automatically
# not just one topic, maybe give option?
#currently sorting by popularity

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
urlCall = ('https://newsapi.org/v2/everything?'
       'q=Artsakh&'
       'from=2023-08-14&' 
       'language=en&'
       'sortBy=popularity&'
       f'apiKey={NEWS_API_KEY}')

response = requests.get(urlCall)
# Take all of this and put it into a separate file, send just the response

if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    # Initialize a set to keep track of unique article titles
    unique_titles = set()
    
    articles = []
    
    for article in data["articles"]:
        if article["title"] != "[Removed]" and article["title"] not in unique_titles:
            articles.append(article)
            unique_titles.add(article["title"])
    
    for article in articles:
        if article["urlToImage"] is None or (isinstance(article["urlToImage"], str) and article["urlToImage"].endswith(".webp")):
            keyword = extractKeywords(article["title"], 1)
            article["urlToImage"] = getImageURL(keyword)

    domains = [urlparse(article["urlToImage"]).netloc for article in articles[:50]]
    domains = [domain.decode("utf-8") if isinstance(domain, bytes) else domain for domain in domains]  # Convert bytes to strings if necessary
else:
    print(f"Request failed with status code: {response.status_code}")



# Write filtered articles to the "newsArticles.json" file
if response.status_code == 200:
    # Define the file path where you want to save the articles in JSON format
    file_path = 'app/news/newsArticles.json'
    # Open the file in write mode and write the filtered articles as JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        file.truncate(0)  # Clear the file's contents
        json.dump(articles[:50], file, ensure_ascii=False, indent=4)

    # Extract domain names from the filtered articles and save to "allowedDomains.json"
    filtered_domains = [urlparse(article["urlToImage"]).netloc for article in articles[:50]]
    filtered_domains = [domain.decode("utf-8") if isinstance(domain, bytes) else domain for domain in filtered_domains]
    with open('app/news/allowedDomains.json', 'w') as json_file:
        json.dump(filtered_domains, json_file)
else:
    print(f'Request failed with status code {response.status_code}')


