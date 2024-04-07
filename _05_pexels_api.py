import requests

# Replace 'YOUR_API_KEY' with your actual Pexels API key
API_KEY = 'LY81GZhabWQTgBaXrQ9yTqL6RlW5If4J34IF6a7QrOfAoVfvlE554qxP'
API_ENDPOINT = 'https://api.pexels.com/v1/search'

# Example search query
query = 'nature'

# Make a GET request to the search endpoint
response = requests.get(API_ENDPOINT, params={'query': query}, headers={'Authorization': API_KEY})

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Access the list of photos
    photos = data['photos']
    # Do something with the photos (e.g., display them)
    for photo in photos:
        print(photo['src']['large'])
else:
    print(f'Error: {response.status_code}')
