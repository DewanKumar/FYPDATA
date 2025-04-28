import json
import random
from pathlib import Path

# Load the original JSON file
file_path = Path("Laptops_06_04_2025.json")
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Filter only items that have a PKR price
pkr_items_indices = [
    idx for idx, item in enumerate(data)
    if "price" in item and isinstance(item["price"], str) and item["price"].startswith("PKR")
]

# Randomly select up to 400 products (or less if not available)
selected_indices = random.sample(pkr_items_indices, min(400, len(pkr_items_indices)))

# Decrease price for selected items
for idx in selected_indices:
    item = data[idx]
    try:
        old_price = int(item["price"].replace("PKR", "").replace(",", "").strip())
        decrease_amount = random.randint(2000, 5000)
        new_price = max(0, old_price - decrease_amount)  # Avoid negative prices
        item["price"] = f"PKR {new_price:,}"
    except Exception as e:
        print(f"Skipping item at index {idx} due to error: {e}")

# Save the updated data to a new JSON file
new_file_path = Path("Laptops_06_04_2025.json")
with open(new_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"✅ Updated file saved as: {new_file_path.name}")
