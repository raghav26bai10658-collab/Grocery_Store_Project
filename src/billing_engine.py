# billing_engine.py
class Cart:
    def __init__(self):
        self.items = [] # Will hold tuples of (Product, quantity)

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.update_stock(-quantity) # Deduct from temporary stock
            print(f"Added {quantity}x {product.name} to cart.")
            return True
        else:
            print(f"Error: Not enough stock for {product.name}. Only {product.stock} left.")
            return False

    def generate_receipt(self):
        print("\n" + "="*30)
        print("       STORE RECEIPT       ")
        print("="*30)
        total = 0.0
        for product, qty in self.items:
            subtotal = product.price * qty
            total += subtotal
            print(f"{product.name:15} x{qty:2}  ₹{subtotal:.2f}")
        
        print("-" * 30)
        print(f"TOTAL AMOUNT:          ₹{total:.2f}")
        print("="*30 + "\n")
        return total