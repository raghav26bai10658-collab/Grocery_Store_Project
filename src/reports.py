# reports.py
def generate_low_stock_report(inventory, threshold=10):
    """Checks the inventory and alerts if any items are below the stock threshold."""
    print("\n--- LOW STOCK REPORT ---")
    low_stock_items = [p for p in inventory.values() if p.stock < threshold]
    
    if not low_stock_items:
        print("All items are sufficiently stocked.")
    else:
        for item in low_stock_items:
            print(f"WARNING: {item.name} is low on stock! (Current: {item.stock})")
    print("------------------------\n")