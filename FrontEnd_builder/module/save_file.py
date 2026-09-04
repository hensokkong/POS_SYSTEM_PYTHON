import json
import os

from DataProduct import products

DATA_FILE = "products.json"
def load_products():
    # JSON file does not exist
    if not os.path.exists(DATA_FILE):
        return products.product_data

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            # JSON exists but is empty []
            if not data:
                return products.product_data

            return data

    except json.JSONDecodeError:
        # JSON is empty or invalid
        return products.product_data
#Save
def save_products(product):
    with open(DATA_FILE, "w") as file:
        json.dump(product, file,indent=4)