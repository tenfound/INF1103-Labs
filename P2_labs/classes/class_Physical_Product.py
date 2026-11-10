from P2_labs.classes.Supplier import Supplier
from P2_labs.classes.class_Can_Be_Shipped import CanBeShipped
from P2_labs.classes.class_Product import Product
class Physical_Product(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def get_weight():
        weight = float(input("Product Weight: "))
        return weight

    def display_information(self):
        return super().display_information() + f", Weight: {self.__weight}"
        # return print(f"Weight: {self.__weight}")

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
        shipping_cost = self.calculate_shipping_cost()
        return (f"Product requires physical shipping, shipping cost per kg: ${shipping_cost:.2f}")

    def calculate_shipping_cost(self):
        cost = (self.__weight % 2) * 2 
        # return self.__weight * 0.5
        return cost