class Product():
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__productid = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        
    def get_name():
        product_id = input("Prodcut ID: ")
        name = input("Product Name: ")
        return product_id, name
    
    def get_price():
        price = input("Product Price: ")
        return price

    def get_stock():
        stock = input("Stock Quantity: ")
        return stock

    def get_product_id(self):
        return self.__productid

    def to_dict(self):
        return {
            "ID" : self.__productid,
            "Name" : self.__name,
            "Price" : self.__price,
            "Stock" : self.__stock
        }

    @classmethod
    def from_dict(cls, item):
        return cls(
            item["ID"], 
            item["Name"], 
            item["Price"], 
            item["Stock"]
        )
    def display_information(self):
        return(f"Product ID: {self.__productid}, Product Name: {self.__name}, Price: ${self.__price}, Stock: {self.__stock}")

    def __str__(self):      # Enables user to read actual values when printing class
        return (f"Product ID: {self.__productid}, Product Name: {self.__name}, Price: ${self.__price}, Stock: {self.__stock}")
    