from P2_labs.classes.OrderLine import OrderLine
from P2_labs.classes.class_Product import Product

class Order:
    def __init__(self, order_id: str):
        self.__orderid: str = order_id
        self.__orderlines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__orderlines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.__orderlines:
            total += order_line.calculate_subtotal()
        return total