if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    # Filter out articles with the title "removed" and extract URLs from the remaining articles
    articles = [article for article in data["articles"] if article["title"] != "[Removed]"]
    for article in articles:
        if article["urlToImage"] is None:
            # Replace it with the URL from the previous API call
            print("hi")
            article["urlToImage"] = exported_image_url  # Replace 'imageUrl' with the actual variable name
        size = get_image_size(article["urlToImage"])
        if size is not None:
            arr.append(size)
    print(arr)
    domains = [urlparse(article["urlToImage"]).netloc for article in articles[:50]]
    domains = [domain.decode("utf-8") if isinstance(domain, bytes) else domain for domain in domains]  # Convert bytes to strings if necessary
else:
    print(f"Request failed with status code: {response.status_code}")