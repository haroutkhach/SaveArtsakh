import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def make_api_call():
    urlCall = (
        'https://newsapi.org/v2/everything?'
        'q=Artsakh&'
        'from=2023-08-15&'
        'language=en&'
        'sortBy=popularity&'
        f'apiKey={NEWS_API_KEY}'
    )

    try:
        response = requests.get(urlCall)
        return response
    except requests.exceptions.RequestException as e:
        print(f"API request failed with error: {e}")
        return None

if __name__ == "__main__":
    response = make_api_call()
    if response:
        with open('api_response.json', 'wb') as file:
            file.write(response.content)
        print("API response saved to 'api_response.json'")
