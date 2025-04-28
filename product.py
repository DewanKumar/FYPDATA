import json
import pandas as pd

# Load the two JSON files
with open("Laptops_17_11_2024.json", "r", encoding="utf-8") as f1, open("Laptops_10_11_2024.json", "r", encoding="utf-8") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

# Function to clean and convert price strings like "PKR 1,234" to integer 1234
def normalize_price(price):
    try:
        return int(str(price).replace("PKR", "").replace(",", "").strip())
    except:
        return None

# Build title:price mappings
normalized_prices1 = {
    item.get("title"): normalize_price(item.get("price"))
    for item in data1 if "title" in item and "price" in item
}
normalized_prices2 = {
    item.get("title"): normalize_price(item.get("price"))
    for item in data2 if "title" in item and "price" in item
}

# Find common titles and compare prices
price_differences = []
for title in set(normalized_prices1) & set(normalized_prices2):
    price1 = normalized_prices1[title]
    price2 = normalized_prices2[title]
    if price1 is not None and price2 is not None and price1 != price2:
        price_differences.append({
            "title": title,
            "price_in_file1": price1,
            "price_in_file2": price2
        })

# Save to CSV if differences found
if price_differences:
    df = pd.DataFrame(price_differences).sort_values(by="title")
    df.to_csv("de.csv", index=False)
    print("✅ Price differences saved to 'de.csv'")
else:
    print("ℹ️ No price differences found between the two files.")
