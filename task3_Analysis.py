import pandas as pd
import numpy as np

# Step 1: Read the CSV file
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print("Data Loaded:", df.shape)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Step 2: Basic analysis (NumPy)

# Calculate the average score
avg_score = np.mean(df["score"])

# Calculate the average number of comments
avg_comments = np.mean(df["num_comments"])

print("\nAverage Score:", round(avg_score, 2))
print("Average Comments:", round(avg_comments, 2))

# NumPy statistics
print("\nNumPy Statistics:")

print("Mean Score:", np.mean(df["score"]))
print("Median Score:", np.median(df["score"]))
print("Standard Deviation:", np.std(df["score"]))
print("Maximum Score:", np.max(df["score"]))
print("Minimum Score:", np.min(df["score"]))

# Step 3: Create new columns

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = True if score > average score
df["is_popular"] = df["score"] > avg_score


# Step 4: Additional insights

# Category with most stories
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print("\nCategory with the most stories:", top_category, "(", count, "stories)")