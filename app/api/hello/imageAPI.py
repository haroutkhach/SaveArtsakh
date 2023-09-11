import requests
import json
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("IMAGE_API_KEY")

def getImageURL(query):
    url = 'https://api.unsplash.com/search/photos'
    params = {
        'query': query,
        'orientation': 'landscape',
        'per_page': 1,
    }

    headers = {
        'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}',
    }

    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                photo = data['results'][0]
                image_url = photo['urls']['regular']
                return image_url
            else:
                print('No photos found.')
        else:
            print(f'Request failed with status code: {response.status_code}')

    except Exception as e:
        print('Something went wrong:', e)
    
    return None
# if __name__ == "__main__":
#     query = 'armenia'
#     image_url = getImageURL(query)
#     print(image_url)