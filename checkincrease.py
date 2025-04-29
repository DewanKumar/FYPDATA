import json
import csv

# Load both JSON files
with open("Asset_03_11_2024.json", "r", encoding="utf-8") as f1, open("Asset_10_11_2024.json", "r", encoding="utf-8") as f2:
    original = json.load(f1)
    updated = json.load(f2)

# Prepare the data
increased = []
for o, u in zip(original, updated):
    try:
        o_price = int(str(o["price"]).replace("PKR", "").replace("Rs.", "").replace(",", "").strip())
        u_price = int(str(u["price"]).replace("PKR", "").replace("Rs.", "").replace(",", "").strip())
        if u_price > o_price:
            increased.append({
                'Product Name': o.get('title', 'Unknown'),
                'Old Price': o_price,
                'New Price': u_price
            })
    except Exception as e:
        continue

# Print the count
print(f"✅ Total prices increased: {len(increased)}")

# Save the increased data into CSV
csv_file = "increased_prices.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Product Name", "Old Price", "New Price"])
    writer.writeheader()
    writer.writerows(increased)

print(f"✅ CSV file '{csv_file}' created successfully.")
