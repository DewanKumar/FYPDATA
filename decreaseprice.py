import json
import random

# Load original file
with open("Asset_06_04_2025.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Filter items with valid numeric price (no PKR, just numbers)
valid_price_indices = [
    idx for idx, item in enumerate(data)
    if "price" in item and isinstance(item["price"], str) and item["price"].replace(",", "").isdigit()
]

# Randomly select 400 items
selected_indices = random.sample(valid_price_indices, min(400, len(valid_price_indices)))

# Decrease prices
for idx in selected_indices:
    item = data[idx]
    try:
        old_price = int(item["price"].replace(",", "").strip())
        decrease_amount = random.randint(2000, 8000)
        new_price = max(old_price - decrease_amount, 0)  # Prevent negative prices
        item["price"] = f"{new_price:,}"  # Format with commas
    except Exception as e:
        print(f"Skipping index {idx} due to error: {e}")

# Save updated file
with open("Asset_06_04_2025.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ Prices decreased and saved to 'Asset_10_11_2024_decreased.json'")
