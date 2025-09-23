# Vibe_Mate - Final Project
# Music Data Analysis

import pandas as pd
import numpy as np

#  Read the main dataset
data = pd.read_csv("dataset.csv")

#  Read the genre, year, and artist datasets (if available, else empty DataFrames)
try:
    genre_data = pd.read_csv("genre_data.csv")
except FileNotFoundError:
    genre_data = pd.DataFrame()

try:
    year_data = pd.read_csv("year_data.csv")
except FileNotFoundError:
    year_data = pd.DataFrame()

try:
    artist_data = pd.read_csv("artist_data.csv")
except FileNotFoundError:
    artist_data = pd.DataFrame()

# Display the first two rows
print("Main Data (first 2 rows):")
print(data.head(2), "\n")

print("Genre Data (first 2 rows):")
print(genre_data.head(2), "\n")

print("Year Data (first 2 rows):")
print(year_data.head(2), "\n")

print("Artist Data (first 2 rows):")
print(artist_data.head(2), "\n")

#  Retrieve info
print("Info of Main Data:")
data.info()
print("\nInfo of Genre Data:")
genre_data.info()

#  Create decade column using apply() and lambda
# Since dataset.csv has no 'year' column, we create a dummy year column for demonstration
if "year" not in data.columns:
    data["year"] = np.random.randint(1970, 2021, size=len(data))

data["decade"] = data["year"].apply(lambda x: (x // 10) * 10)

print("\nMain Data with Year and Decade columns added:")
print(data[["year", "decade"]].head(10))

