from app.models import Order, OrderStatus

class OrderProcessor:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager

    def process_order(self, order: Order) -> Order:
        deducted_items = []
        for order_item in order.items:
            success = self.inventory.deduct_stock(order_item.item_id, order_item.quantity)
            
            if not success:
                for item in deducted_items:
                    self.inventory.restore_stock(item.item_id, item.quantity)
                order.status = OrderStatus.FAILED
                order.error_message = f"Item {order_item.item_id} is out of stock."
                return order
            deducted_items.append(order_item)
        
        order.status = OrderStatus.COMPLETED
        return order
