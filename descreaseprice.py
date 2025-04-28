import json
import random
from pathlib import Path

file_path = Path("Czone_13_04_2025.json")
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

pkr_items_indices = [
    idx for idx, item in enumerate(data)
    if "price" in item and isinstance(item["price"], str) and item["price"].startswith(("PKR", "Rs."))
]

selected_indices = random.sample(pkr_items_indices, min(400, len(pkr_items_indices)))

for idx in selected_indices:
    item = data[idx]
    try:
        old_price = int(item["price"].replace("PKR", "").replace("Rs.", "").replace(",", "").strip())
        decrease_amount = random.randint(2000, 5000)
        new_price = max(0, old_price - decrease_amount)
        item["price"] = f"Rs.{new_price:,}"
    except Exception as e:
        print(f"Skipping item at index {idx} due to error: {e}")

# Save new file
new_file_path = Path("Czone__04_2025.json")
with open(new_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"✅ Price decreased file saved as {new_file_path.name}")
