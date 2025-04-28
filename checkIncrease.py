import json
import pandas as pd

with open("paklap_10_11_2024.json", "r", encoding="utf-8") as f1, open("paklap_03_11_2024.json", "r", encoding="utf-8") as f2:
    new_data = json.load(f1)
    old_data = json.load(f2)

def normalize_price(price):
    try:
        return int(str(price).replace("PKR", "").replace("Rs.", "").replace(",", "").replace(".00", "").strip())
    except:
        return None

new_prices = {item.get("title"): normalize_price(item.get("price")) for item in new_data if "title" in item and "price" in item}
old_prices = {item.get("title"): normalize_price(item.get("price")) for item in old_data if "title" in item and "price" in item}

price_increases = []
for title in set(new_prices) & set(old_prices):
    new_price = new_prices[title]
    old_price = old_prices[title]
    if new_price is not None and old_price is not None and new_price > old_price:
        price_increases.append({
            "title": title,
            "old_price": old_price,
            "new_price": new_price,
            "increase_amount": new_price - old_price
        })

if price_increases:
    df = pd.DataFrame(price_increases).sort_values(by="title")
    df.to_csv("price_increased_paklap.csv", index=False)
    print("✅ Price increases saved to 'price_increased_paklap.csv'")
else:
    print("ℹ️ No price increases found.")
