import pandas as pd
import random

# Load the cleaned food truck data (replace with your actual data file)
df = pd.read_csv("cleaned_food_trucks_data.csv")

# Define a list of days and times
days = ['Saturday', 'Sunday']
times = ['9:00 AM', '12:00 PM', '3:00 PM', '6:00 PM', '9:00 PM']

# Initialize an empty plan
foodie_plan = []

# Generate a two-day weekend foodie plan
for day in days:
    for time in times:
        # Randomly select a food truck from the dataset
        food_truck = df.sample(n=1)
        
        # Extract details from the selected food truck
        name = food_truck.iloc[0]['Name']
        address = food_truck.iloc[0]['Address']
        cuisine = food_truck.iloc[0]['Cuisine']
        rating = food_truck.iloc[0]['Rating']

        # Calculate travel time and distance (for illustration, use random values)
        travel_time = f"{random.randint(5, 30)} mins"
        travel_distance = f"{round(random.uniform(0.1, 2.0), 1)} miles"

        # Randomly select a transportation type
        transportation_types = ['Walk', 'Bike', 'Car']
        transportation_type = random.choice(transportation_types)

        # Append the details to the foodie plan
        foodie_plan.append({
            'Day': day,
            'Time': time,
            'Name': name,
            'Address': address,
            'Cuisine': cuisine,
            'Rating': rating,
            'Travel Time': travel_time,
            'Travel Distance': travel_distance,
            'Transportation Type': transportation_type
        })

# Create a DataFrame from the plan
df_foodie_plan = pd.DataFrame(foodie_plan)

# Save the foodie plan data to a CSV file
df_foodie_plan.to_csv("foodie_plan.csv", index=False)
