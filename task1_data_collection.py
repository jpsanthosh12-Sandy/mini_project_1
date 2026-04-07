import requests
import time
import json
import os
from datetime import datetime

# STEP 1: Get top story IDs
try:
    res = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    ids = res.json()[:50]
    print("Got", len(ids), "IDs")
except:
    print("Error getting IDs")
    ids = []

# STEP 2: Get story details
stories = []

for i in ids:
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{i}.json"
        data = requests.get(url).json()

        if data and "title" in data:
            stories.append(data)
    except:
        print("Skip", i)

print("Got", len(stories), "stories")

# STEP 3: Categories (same as image)
categories = {
    "technology": ["ai", "tech", "software", "code","data","API","GPU","LLM"],
    "sports": ["game", "team", "player","FIFA","Kho-kho","cricket","winner","league"],
    "science": ["research", "space", "study","physics","biology","NASA" ,"medical"],
    "worldnews":["war","government","country","president","election","climate","attack","global"],
    "entertainment":["movies","film","vedio games","book","streaming","netfilx"]
}

# STEP 4: Filter and collect data
#categories short form "cat"

result = []

for cat, words in categories.items():
    count = 0

    for s in stories:
        if count == 25:   # 25 per category
            break

        #convert all the words to lower case

        title = s.get("title", "").lower()

        # check keywords
        if any(word in title for word in words):
            result.append({
                "post_id": s.get("id"),
                "title": s.get("title"),
                "category": cat,
                "score": s.get("score", 0),
                "num_comments": s.get("descendants", 0),
                "author": s.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            count += 1

    print(cat, ":", count, "collected")

    # wait 2 seconds
    time.sleep(2)

# STEP 5: Save file
os.makedirs("data", exist_ok=True)

file_name = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

with open(file_name, "w") as f:
    json.dump(result, f, indent=4)

# STEP 6: Final output
print("\nTotal:", len(result))
print("Saved:", file_name)