import json
import pandas as pd

# Load JSON files
with open("Laptops_09_02_2025.json", "r", encoding="utf-8") as f1, open("Laptops_02_02_2025.json", "r", encoding="utf-8") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

# Function to clean and convert price strings like "PKR 1,234" to integer 1234
def normalize_price(price):
    try:
        return int(str(price).replace("PKR", "").replace(",", "").strip())
    except:
        return None

# Build title:price mappings with normalized prices
normalized_prices1 = {
    item.get("title"): normalize_price(item.get("price"))
    for item in data1 if "title" in item and "price" in item
}
normalized_prices2 = {
    item.get("title"): normalize_price(item.get("price"))
    for item in data2 if "title" in item and "price" in item
}

# Find common titles and check if price increased
price_increased = []
for title in set(normalized_prices1) & set(normalized_prices2):
    price1 = normalized_prices1[title]
    price2 = normalized_prices2[title]
    if price1 is not None and price2 is not None and price1 > price2:
        price_increased.append({
            "title": title,
            "old_price": price2,
            "new_price": price1,
            "increase_amount": price1 - price2
        })

# Save to CSV if increased prices found
if price_increased:
    df = pd.DataFrame(price_increased).sort_values(by="title")
    df.to_csv("price_increased_confirmation.csv", index=False)
    print("✅ Price increases saved to 'price_increased_confirmation.csv'")
else:
    print("ℹ️ No price increases found between the two files.")
