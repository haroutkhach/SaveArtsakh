import requests
import json
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
API_KEY = os.getenv("API_KEY")
urlCall = ('https://newsapi.org/v2/everything?'
       'q=Artsakh&'
       'from=2023-08-06&'
       'language=en&'
       'sortBy=popularity&'
       f'apiKey={API_KEY}')

response = requests.get(urlCall)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    # Filter out articles with the title "removed" and extract URLs from the remaining articles
    articles = [article for article in data["articles"] if article["title"] != "[Removed]" and article["urlToImage"] is not None]
    domains = [urlparse(article["urlToImage"]).netloc for article in articles[:50]]
    domains = [domain.decode("utf-8") if isinstance(domain, bytes) else domain for domain in domains]  # Convert bytes to strings if necessary
else:
    print(f"Request failed with status code: {response.status_code}")

# Write filtered articles to the "news_articles.json" file
if response.status_code == 200:
    # Define the file path where you want to save the articles in JSON format
    file_path = 'app/news/news_articles.json'

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


# import json
# from urllib.parse import urlparse

# # Function to extract domains from a list of URLs
# def extract_domains_from_urls(url_list):
#     allowed_domains = []
#     for url in url_list:
#         parsed_url = urlparse(url)
#         domain = parsed_url.netloc
#         allowed_domains.append(domain)
#     return allowed_domains

# # Read URLs from a text file (one URL per line)
# input_file = "urls.txt"  # Replace with the path to your input file
# with open(input_file, "r") as file:
#     urls = file.read().splitlines()

# # Extract domains from the URLs
# domains = extract_domains_from_urls(urls)

# # Write the list of domains to a JSON file
# output_file = "allowedDomains.json"
# with open(output_file, "w") as json_file:
#     json.dump(domains, json_file, indent=4)

# print(f"Domains extracted and saved to {output_file}")
