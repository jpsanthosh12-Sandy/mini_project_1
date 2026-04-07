import pandas as pd
import matplotlib.pyplot as plt
import os

# STEP 1: Load data
df = pd.read_csv("data/trends_analyzed.csv")

print("Data loaded:", df.shape)

# Create output folder
os.makedirs("outputs", exist_ok=True)


# STEP 2: Chart 1 - Top 10 Stories by Score

# Sort and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Short titles (first 50 characters)
top10["short_title"] = top10["title"].str[:50]

plt.figure()

plt.barh(top10["short_title"], top10["score"])

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Title")

# Show highest score on top
plt.gca().invert_yaxis()

# Save chart
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# STEP 3: Chart 2 - Stories per Category

category_counts = df["category"].value_counts()

plt.figure()

plt.bar(category_counts.index, category_counts.values)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")

# Save chart
plt.savefig("outputs/chart2_categories.png")
plt.close()


# STEP 4: Chart 3 - Score vs Comments

plt.figure()

plt.scatter(df["score"], df["num_comments"])

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Comments")

# Save chart
plt.savefig("outputs/chart3_scatter.png")
plt.close()


print("\nAll charts saved in 'outputs' folder")