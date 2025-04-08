import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ----------------------------------
# 1. Create a small training dataset
# ----------------------------------

data = {
    'Rainfall_mm': [200, 180, 90, 75, 250, 100, 300, 120],
    'Elevation_m': [120, 140, 300, 400, 100, 320, 90, 310],
    'Slope_deg': [5, 10, 25, 20, 4, 27, 3, 23],
    'Distance_to_river_km': [0.5, 1.2, 6.0, 5.5, 0.3, 7.0, 0.2, 5.8],
    'Flood_Prone': [1, 1, 0, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# -------------------------------
# 2. Prepare features and labels
# -------------------------------

X = df[['Rainfall_mm', 'Elevation_m', 'Slope_deg', 'Distance_to_river_km']]
y = df['Flood_Prone']

# -------------------------------
# 3. Train the model
# -------------------------------

model = DecisionTreeClassifier()
model.fit(X, y)

# -------------------------------
# 4. Take user input interactively
# -------------------------------

print("Enter details to check flood risk:\n")

rainfall = float(input("Rainfall (mm): "))
elevation = float(input("Elevation (m): "))
slope = float(input("Slope (degrees): "))
distance = float(input("Distance to river (km): "))

# Prepare input for prediction
user_input = [[rainfall, elevation, slope, distance]]

# -------------------------------
# 5. Predict and display result
# -------------------------------

prediction = model.predict(user_input)

if prediction[0] == 1:
    print("\n  The area is likely to be **FLOOD PRONE**.")
else:
    print("\n The area is **NOT flood prone**.")
