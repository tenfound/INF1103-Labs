from class_Can_Be_Shipped import CanBeShipped
from class_Product import Product
class Physical_Product(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        weight = float(input("Product Weight: "))
        return weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}")

    def to_dict(self):
        data = super().to_dict()
        data["Weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, item):
        return cls(
            item["ID"],
            item["Name"],
            item["Price"],
            item["Stock"],
            item["Weight"],
        )

    def get_fulfillment_info(self):
        return (f"Product requires physical shipping")
        
    def calculate_shipping_cost(self):
        shipping_cost = self.__weight * 0.5
        return shipping_cost