# main.py
from models import Product
import storage_handler
from billing_engine import Cart
import reports

def display_menu():
    print("\n--- GROCERY STORE MANAGEMENT SYSTEM ---")
    print("1. View Inventory")
    print("2. Add New Product (Admin)")
    print("3. Make a Sale (Cashier)")
    print("4. Generate Low Stock Report (Analytics)")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def main():
    # Initialization and Setup
    storage_handler.initialize_database()
    inventory = storage_handler.load_all_products()

    while True:
        choice = display_menu()

        if choice == '1':
            print("\n--- Current Inventory ---")
            if not inventory:
                print("Inventory is currently empty.")
            for prod_id, product in inventory.items():
                print(product.display_info())

        elif choice == '2':
            print("\n--- Add New Product ---")
            p_id = input("Enter Product ID: ")
            if p_id in inventory:
                print("Error: Product ID already exists. Please use a unique ID.")
                continue
                
            name = input("Enter Product Name: ")
            try:
                price = float(input("Enter Price: ₹"))
                stock = int(input("Enter Stock Quantity: "))
                new_product = Product(p_id, name, price, stock)
                inventory[p_id] = new_product
                storage_handler.save_new_product(new_product)
                print(f"[{name}] added successfully!")
            except ValueError:
                print("Error: Price and Stock must be valid numbers.")

        elif choice == '3':
            cart = Cart()
            print("\n--- Point of Sale ---")
            while True:
                item_id = input("Enter Product ID (or 'done' to finish): ")
                if item_id.lower() == 'done':
                    break
                
                if item_id in inventory:
                    try:
                        qty = int(input(f"Enter quantity for {inventory[item_id].name}: "))
                        if qty <= 0:
                            print("Error: Quantity must be greater than 0.")
                            continue
                        cart.add_to_cart(inventory[item_id], qty)
                    except ValueError:
                        print("Error: Quantity must be a valid number.")
                else:
                    print("Error: Product ID not found in inventory.")
            
            if cart.items:
                cart.generate_receipt()
                storage_handler.update_inventory_file(inventory)
                print("Inventory database updated successfully.")
                
        elif choice == '4':
            reports.generate_low_stock_report(inventory, threshold=20)

        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()