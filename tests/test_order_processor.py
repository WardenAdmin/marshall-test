import pytest
from app.models import Order, OrderItem, OrderStatus
from app.inventory_manager import InventoryManager
from app.order_processor import OrderProcessor

def test_successful_multi_item_order():
    inv = InventoryManager()
    processor = OrderProcessor(inv)
    
    order = Order(
        order_id="ord-001",
        items=[
            OrderItem("item_alpha", 2),
            OrderItem("item_beta", 1)
        ]
    )
    
    processed = processor.process_order(order)
    assert processed.status == OrderStatus.COMPLETED
    assert inv.get_stock("item_alpha") == 8
    assert inv.get_stock("item_beta") == 4

def test_failed_order_inventory_leak():
    inv = InventoryManager()
    processor = OrderProcessor(inv)
    
    order = Order(
        order_id="ord-002",
        items=[
            OrderItem("item_alpha", 3),
            OrderItem("item_gamma", 1)
        ]
    )
    
    processed = processor.process_order(order)
    
    assert processed.status == OrderStatus.FAILED
    assert "out of stock" in processed.error_message.lower()
    assert inv.get_stock("item_alpha") == 10, "Inventory leaked! Deducted stock was never restored on failure."
