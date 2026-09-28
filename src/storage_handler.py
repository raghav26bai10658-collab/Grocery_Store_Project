# storage_handler.py
import csv
import os
from models import Product

INVENTORY_FILE = "inventory.csv"

def initialize_database():
    """Creates the CSV file with headers if it does not exist."""
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["product_id", "name", "price", "stock"])
        print("Database initialized.")

def save_new_product(product):
    """Appends a new product object to the CSV file."""
    with open(INVENTORY_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product.product_id, product.name, product.price, product.stock])

def load_all_products():
    """Reads the CSV and returns a dictionary of Product objects."""
    inventory = {}
    if not os.path.exists(INVENTORY_FILE):
        return inventory
        
    with open(INVENTORY_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = Product(row["product_id"], row["name"], row["price"], row["stock"])
            inventory[row["product_id"]] = item
            
    return inventory

def update_inventory_file(inventory):
    """Overwrites the CSV with the updated stock levels."""
    with open(INVENTORY_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["product_id", "name", "price", "stock"])
        for product in inventory.values():
            writer.writerow([product.product_id, product.name, product.price, product.stock])