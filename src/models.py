# models.py
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def display_info(self):
        """Returns a formatted string of the product's details."""
        return f"[{self.product_id}] {self.name} - ₹{self.price:.2f} (Stock: {self.stock})"

    def update_stock(self, amount):
        """Updates the stock quantity."""
        self.stock += amount