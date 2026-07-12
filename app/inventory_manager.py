from typing import Dict

class InventoryManager:
    def __init__(self):
        self._stock: Dict[str, int] = {
            "item_alpha": 10,
            "item_beta": 5,
            "item_gamma": 0
        }

    def get_stock(self, item_id: str) -> int:
        return self._stock.get(item_id, 0)

    def set_stock(self, item_id: str, quantity: int):
        self._stock[item_id] = quantity

    def deduct_stock(self, item_id: str, quantity: int) -> bool:
        current = self.get_stock(item_id)
        if current >= quantity:
            self._stock[item_id] = current - quantity
            return True
        return False
