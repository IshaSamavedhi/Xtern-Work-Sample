# need to pip install geopy folium !!

import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Sample travel route data (replace with your own data)
locations = [
    ('Starting Point', 'IUPUI, Indianapolis, IN'),
    ('Food Truck 1', 'Address 1, Indianapolis, IN'),
    ('Food Truck 2', 'Address 2, Indianapolis, IN'),
    ('Food Truck 3', 'Address 3, Indianapolis, IN'),
]

# Create a map centered at the starting point
geolocator = Nominatim(user_agent="foodie_plan")
starting_point = geolocator.geocode(locations[0][1])
m = folium.Map(location=[starting_point.latitude, starting_point.longitude], zoom_start=14)

# Add markers for each location
for location in locations:
    coords = geolocator.geocode(location[1])
    folium.Marker(
        location=[coords.latitude, coords.longitude],
        popup=location[0]
    ).add_to(m)

# Calculate and add travel routes
total_distance = 0
for i in range(1, len(locations)):
    start = geolocator.geocode(locations[i - 1][1])
    end = geolocator.geocode(locations[i][1])
    distance = geodesic((start.latitude, start.longitude), (end.latitude, end.longitude)).miles
    total_distance += distance

    folium.PolyLine(
        locations=[(start.latitude, start.longitude), (end.latitude, end.longitude)],
        color='blue',
        weight=2.5,
        opacity=1
    ).add_to(m)

# Display the total travel distance
folium.Marker(
    location=[starting_point.latitude, starting_point.longitude],
    popup=f'Total Distance: {round(total_distance, 2)} miles',
    icon=folium.DivIcon(html=f'<div>{round(total_distance, 2)} miles</div>')
).add_to(m)

# Save the map to an HTML file
m.save('travel_route_map.html')
