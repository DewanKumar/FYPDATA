import json
import pandas as pd

# Load the two JSON files
with open("Laptops_08_12_2024.json", "r", encoding="utf-8") as f1, open("Laptops_01_12_2024.json", "r", encoding="utf-8") as f2:
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

# Find common titles and compare prices (only decrease)
price_decreases = []
for title in set(normalized_prices1) & set(normalized_prices2):
    price1 = normalized_prices1[title]  # Price in new decreased file
    price2 = normalized_prices2[title]  # Price in old original file
    if price1 is not None and price2 is not None and price1 < price2:
        price_decreases.append({
            "title": title,
            "old_price": price2,
            "new_price": price1,
            "decrease_amount": price2 - price1
        })

# Save to CSV if decreases found
if price_decreases:
    df = pd.DataFrame(price_decreases).sort_values(by="title")
    df.to_csv("decreased_prices.csv", index=False)
    print("✅ Decreased prices saved to 'decreased_prices.csv'")
else:
    print("ℹ️ No price decreases found between the two files.")
