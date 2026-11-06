from class_Product import Product
class Digital_Product(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        download_size = float(input("Product Download Size: "))
        return download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size}")

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
            return (f"Product requires physical shipping")