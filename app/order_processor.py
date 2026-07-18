from app.models import Order, OrderStatus

class OrderProcessor:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager

    def process_order(self, order: Order) -> Order:
        for order_item in order.items:
            success = self.inventory.deduct_stock(order_item.item_id, order_item.quantity)
            
            if not success:
                order.status = OrderStatus.FAILED
                order.error_message = f"Item {order_item.item_id} is out of stock."
                for order_item in order.items:
                    self.inventory.restore_stock(order_item.item_id, order_item.quantity)
                return order
        
        order.status = OrderStatus.COMPLETED
        return order
