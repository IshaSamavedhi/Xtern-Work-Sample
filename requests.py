import requests

# Replace 'YOUR_API_KEY' with your actual Google API Key
api_key = 'AIzaSyAxetAaSuEdet3FGjaDRaTPZqC3WlpfUc8'

# Define the API endpoint for searching food trucks
api_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Set the parameters for your search
params = {
    'location': 'latitude,longitude',  # Replace with the coordinates of your target location
    'radius': '1000',  # Define the search radius in meters
    'keyword': 'food truck',
    'key': api_key,
}

# Make an API request to Google Places API
response = requests.get(api_url, params=params)

# Parse the JSON response
data = response.json()

# Extract relevant information from the response
food_trucks = data.get('results', [])

for truck in food_trucks:
    print(f"Name: {truck['name']}")
    print(f"Address: {truck['vicinity']}")
    print(f"Rating: {truck.get('rating', 'N/A')}")
    print(f"Website: {truck.get('website', 'N/A')}")
    print("\n")