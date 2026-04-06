import pandas as pd
import json

# STEP 1: Load JSON file
file_path = "data/trends_20260406.json"   

#converting to json file

with open(file_path, "r") as f:
    data = json.load(f)

# converting to dataframe

df = pd.DataFrame(data)

print("Total rows loaded:", len(df))


# STEP 2: Clean Data

# Remove duplicate data
df = df.drop_duplicates(subset="post_id")

# Remove rows with missing values
df = df.dropna(subset=["post_id", "title", "score"])

# Convert score and comments to numbers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Keep only rows where score >= 5
df = df[df["score"] >= 5]

# Remove extra spaces in title
df["title"] = df["title"].str.strip()

print("Rows after cleaning:", len(df))


# STEP 3: Save as CSV
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print("File saved as:", output_file)


# STEP 4: Show summary
print("\nStories per category:")
print(df["category"].value_counts())