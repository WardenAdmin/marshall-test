from typing import Dict


class InventoryManager:
    def __init__(self):
        # Stock is internal. External code may only use dedicated domain methods.
        self._stock: Dict[str, int] = {
            "item_alpha": 10,
            "item_beta": 5,
            "item_gamma": 0,
        }

    def deduct_stock(self, item_id: str, quantity: int) -> bool:
        current = self._stock.get(item_id, 0)
        if current >= quantity:
            self._stock[item_id] = current - quantity
            return True
        return False

    def restore_stock(self, item_id: str, quantity: int) -> None:
        current = self._stock.get(item_id, 0)
        self._stock[item_id] = current + quantity
