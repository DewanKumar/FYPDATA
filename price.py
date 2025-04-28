import json
import random

# Load JSON file
file_path = 'Laptops_17_11_2024.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Identify products list
products = data if isinstance(data, list) else next(v for v in data.values() if isinstance(v, list))

# Fix the random seed (optional for reproducibility)
# random.seed(42)

# Select exactly 400 unique products
selected_indices = random.sample(range(len(products)), 400)

# Helper functions
def clean_price(p):
    try:
        return int(str(p).replace("PKR", "").replace(",", "").strip())
    except:
        return None

def format_price(p):
    return f"PKR {p:,}"

# Update prices
for idx in selected_indices:
    original_price = clean_price(products[idx].get('price'))
    if original_price is not None:
        increase = random.randint(2000, 8000)
        new_price = original_price + increase
        products[idx]['price'] = format_price(new_price)

# Save file
updated_path = 'Laptops_17_11_2024.json'
with open(updated_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

updated_path
