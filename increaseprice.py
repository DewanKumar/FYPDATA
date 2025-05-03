import json
import random
from pathlib import Path

# Load original file
with open("Asset_30_03_2025.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Filter items with valid numeric price (string numbers)
pkr_items_indices = [
    idx for idx, item in enumerate(data)
    if "price" in item and isinstance(item["price"], str) and item["price"].replace(",", "").isdigit()
]

# Randomly select 400 items
selected_indices = random.sample(pkr_items_indices, min(400, len(pkr_items_indices)))

# Increase prices
for idx in selected_indices:
    item = data[idx]
    try:
        old_price = int(item["price"].replace(",", "").strip())
        new_price = old_price + random.randint(2000, 8000)
        item["price"] = f"{new_price:,}"  # Keep same format (comma separated)
    except Exception as e:
        print(f"Skipping index {idx} due to error: {e}")

# Save updated file
with open("Asset_30_03_2025.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
