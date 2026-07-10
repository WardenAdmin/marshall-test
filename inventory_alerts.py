def get_low_stock_items(items, threshold):
    low_stock_items = []
    for item in items:
        if item['quantity'] <= threshold:  # Include threshold value
            low_stock_items.append(item)
    return low_stock_items