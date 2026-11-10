class OrderLine:
    def __init__(self, product = str, quantity = int):
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.price  * self.__quantity