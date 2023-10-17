import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

df = pd.read_csv("cleaned_food_trucks_data.csv")

#Distribution of Ratings (Histogram):

cuisine_avg_rating = df.groupby('Cuisine')['Rating'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title('Distribution of Food Truck Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

#Top-Rated vs. Lowest-Rated Food Trucks (Bar Plot):

top_rated = df.nlargest(5, 'Rating')  # Get the top 5 rated food trucks
lowest_rated = df.nsmallest(5, 'Rating')  # Get the lowest 5 rated food trucks

plt.figure(figsize=(12, 6))
sns.barplot(data=top_rated, x='Rating', y='Name', palette='viridis')
plt.title('Top-Rated Food Trucks')
plt.xlabel('Rating')
plt.ylabel('Name')
plt.show()


plt.figure(figsize=(12, 6))
sns.barplot(data=lowest_rated, x='Rating', y='Name', palette='viridis')
plt.title('Lowest-Rated Food Trucks')
plt.xlabel('Rating')
plt.ylabel('Name')
plt.show()

#Cuisine Distribution (Pie Chart):

cuisine_counts = df['Cuisine'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(cuisine_counts, labels=cuisine_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribution of Food Truck Cuisines')
plt.show()

#Average Rating by Cuisine (Bar Plot):

cuisine_avg_rating = df.groupby('Cuisine')['Rating'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=cuisine_avg_rating, x='Cuisine', y='Rating')
plt.xticks(rotation=45)
plt.title('Average Ratings of Food Trucks by Cuisine')
plt.xlabel('Cuisine')
plt.ylabel('Average Rating')
plt.show()

#Geospatial Analysis (Folium for interactive maps):

# Create a map centered at IUPUI
m = folium.Map(location=[39.7726, -86.1751], zoom_start=15)

# Add markers for food truck locations
for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m)

m.save('food_truck_map.html')

#Heatmap

corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()