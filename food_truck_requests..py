import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Google API Key
api_key = 'AIzaSyAxetAaSuEdet3FGjaDRaTPZqC3WlpfUc8'

# Define the API endpoint for searching food trucks
api_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Set the parameters for your search
params = {
    'location': '39.7726,-86.1751',  # IUPUI coordinates
    'radius': '1000',  
    'keyword': 'food truck',
    'key': api_key,
}

# Make an API request to Google Places API
response = requests.get(api_url, params=params)

# Parse the JSON response
data = response.json()

# Extract relevant information from the response
food_trucks = data.get('results', [])

# Create a list to store the organized data
organized_data = []

for truck in food_trucks:
    name = truck.get('name', 'N/A')
    address = truck.get('vicinity', 'N/A')
    rating = truck.get('rating', 'N/A')
    website = truck.get('website', 'N/A')  # You may need to extract website information differently
    hours = 'N/A'  # You may need to extract hours information differently
    cuisine = 'N/A'  # You may need to extract cuisine information differently

    # Append the data for this food truck to the list
    organized_data.append({
        'Name': name,
        'Address': address,
        'Rating': rating,
        'Website': website,
        'Hours': hours,
        'Cuisine': cuisine
    })

# Create a DataFrame from the organized data
df = pd.DataFrame(organized_data)

# Drop rows with missing values
df_cleaned = df.dropna()

# Save the cleaned and organized data to a CSV file
df_cleaned.to_csv("cleaned_food_trucks_data.csv", index=False)
