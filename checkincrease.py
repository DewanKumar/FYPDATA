import json
import csv

# Load original and updated files
with open("product_03_11_2024.json", "r", encoding="utf-8") as f1, open("product_10_11_2024.json", "r", encoding="utf-8") as f2:
    original = json.load(f1)
    updated = json.load(f2)

# Collect increased price items
increased = []
for o, u in zip(original, updated):
    try:
        o_price = int(o["price"].replace(",", "").strip())
        u_price = int(u["price"].replace(",", "").strip())
        if u_price > o_price:
            increased.append({
                "Product Name": o.get("title", "Unknown"),
                "Old Price": o_price,
                "New Price": u_price
            })
    except:
        continue

# Output results
print(f"✅ Total prices increased: {len(increased)}")

# Save to CSV
with open("product_data_price_increased.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Product Name", "Old Price", "New Price"])
    writer.writeheader()
    writer.writerows(increased)

print("✅ CSV 'product_data_price_increased.csv' created successfully.")
