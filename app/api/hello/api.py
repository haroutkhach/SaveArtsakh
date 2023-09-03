import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
url = ('https://newsapi.org/v2/everything?'
       'q=Artsakh&'
       'from=2023-08-03&' # evenutally this changes every week
       'language=en&'
       'sortBy=popularity&'
       f'apiKey={API_KEY}')

response = requests.get(url)
print(response.text)
if response.status_code == 200:
    # Extract the JSON content from the response
    news_data = response.json()

    # Define the file path where you want to save the articles in JSON format
    file_path = 'app/news/news_articles.json'

    # Open the file in write mode and write the articles as JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        file.truncate(0)  # Clear the file's contents
        json.dump(news_data, file, ensure_ascii=False, indent=4)

else:
    print(f'Request failed with status code {response.status_code}')