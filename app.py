# app.py
def get_low_stock_items(inventory: list[dict], threshold: int = 5) -> list[str]:
    """
    Returns a list of item names whose quantity is at or below the threshold.
    """
    low_stock = []
    for item in inventory:
        if item["quantity"] <= threshold:
            low_stock.append(item["name"])
    return low_stock
