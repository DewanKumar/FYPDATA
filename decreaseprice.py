import json
import random

# Load original file
with open("product_30_03_2025.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find valid price entries
valid_indices = [
    idx for idx, item in enumerate(data)
    if "price" in item and isinstance(item["price"], str) and item["price"].replace(",", "").isdigit()
]

# Randomly choose 400 items
selected = random.sample(valid_indices, min(400, len(valid_indices)))

# Decrease prices in range 2000–5000
for idx in selected:
    try:
        item = data[idx]
        price = int(item["price"].replace(",", "").strip())
        decrease = random.randint(2000, 5000)
        new_price = max(price - decrease, 0)
        item["price"] = f"{new_price:,}"
    except Exception as e:
        print(f"Skipping index {idx}: {e}")

# Save back to the same file
with open("product_30_03_2025.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
