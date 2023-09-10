import os
import json

# Make file path OS/local machine independent
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
print(ROOT_PATH)
path = os.path.join(ROOT_PATH, "files", "products.json")  # in this example files is a directory name
print(path)

# Deserialize the data from JSON
with open(path, 'r') as products_data:
    products = json.load(products_data)

print(products)

PRODUCT = products['product_name']
print(PRODUCT)

# Change the product name
products['product_name'] = 'xiaomi'

# Serialize the data to JSON
with open(path, 'w') as products_data:
    json.dump(products, products_data)