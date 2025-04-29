import csv
import json
import random

# Load original and decreased files
with open("Asset_17_11_2024.json", "r", encoding="utf-8") as f1, open("Asset_24_11_2024.json", "r", encoding="utf-8") as f2:
    original = json.load(f1)
    decreased = json.load(f2)

# Compare prices
decreased_items = []
for o, d in zip(original, decreased):
    try:
        o_price = int(str(o["price"]).replace(",", "").strip())
        d_price = int(str(d["price"]).replace(",", "").strip())
        if d_price < o_price:
            decreased_items.append({
                'Product Name': o.get('title', 'Unknown'),
                'Old Price': o_price,
                'New Price': d_price
            })
    except:
        continue

# Print count
print(f"✅ Total prices decreased: {len(decreased_items)}")

# Save to CSV
csv_file = "decreased_prices.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Product Name", "Old Price", "New Price"])
    writer.writeheader()
    writer.writerows(decreased_items)

print(f"✅ CSV file '{csv_file}' created successfully.")
