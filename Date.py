import json
from pathlib import Path

# Load the original JSON file
input_file = Path("czone-laptops.json")
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Add the same date to each product
for product in data:
    product["date"] = "2025-04-27"

# Save to a new file
output_file = Path("Czone_27_04_2025.json")
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("New file with date column created successfully!")
