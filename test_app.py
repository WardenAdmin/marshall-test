from app import get_low_stock_items

def test_get_low_stock_items_below_threshold():
    inventory = [
        {"name": "Widget A", "quantity": 2},
        {"name": "Widget B", "quantity": 10}
    ]
    # Passes because 2 < 5
    assert get_low_stock_items(inventory, threshold=5) == ["Widget A"]

def test_get_low_stock_items_at_threshold():
    inventory = [
        {"name": "Widget C", "quantity": 5},
        {"name": "Widget D", "quantity": 1}
    ]
    assert get_low_stock_items(inventory, threshold=5) == ["Widget C", "Widget D"]
