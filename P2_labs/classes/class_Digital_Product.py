from P2_labs.classes.class_Product import Product
from P2_labs.classes.Supplier import Supplier
class Digital_Product(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def get_download_size():
        download_size = float(input("Product Download Size: "))
        return download_size

    def display_information(self):
        return super().display_information() + f", Download Size: {self.__download_size} MB"

    def to_dict(self):
        data = super().to_dict()
        data["Download Size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, item):
        return cls(
            item["ID"],
            item["Name"],
            item["Price"],
            item["Stock"],
            item["Download Size"]
        )

    def get_fulfillment_info(self):
            return (f"Product does not require physical shipping, download size: {self.__download_size} MB")