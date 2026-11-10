import json
from P2_labs.classes.class_Product import Product
class Inventory():
    def __init__(self):
        self.__products: list[Product] = []
        self.__past_products: list[Product] = []

    def load_inventory(self):
        with open("inventory2.json", "r") as f:
            loaded_inventory = json.load(f)
        return loaded_inventory

    def add_product(self, product: Product):
        self.__products.append(product)

    def remove_product(self, product: Product):
        remove_product = self.search_product(product.get_product_id())
        for p in self.__products:
            if p.get_product_id() == remove_product.get_product_id():
                self.__products.pop(self.__products.index(p))
                print(f"Product {remove_product.get_product_id()} removed from inventory.")
        else:
            print("Product not found in inventory.")
        
    def search_product(self, searched_product_id):
        data = self.load_inventory()
        self.__past_products = [Product.from_dict(item) for item in data]
        for product in self.__past_products:
            if product.get_product_id() == searched_product_id:
                return product
        print("Product not found")
        return None

    def display_all(self):
        self.__past_products = self.load_inventory()
        for p in self.__past_products:
            print(p)

    def save_inventory(self):
        # for product in self.__products:
        with open("inventory2.json", "w") as f:
                json.dump([x.to_dict() for x in self.__products], f, indent=4)

    def inventory_length(self):
        if len(self.__products) == 0:
            return "empty"