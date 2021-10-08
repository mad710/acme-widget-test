
class Product:
    """
    Product class
    """
    
    def __init__(self, code: str, name: str, price: float):
        """
        Returns a new product object
        
        :param code str: Product code
        :param name str: Name of the product
        :param price str: Product price in dollars
        """
        self.code = code
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.product} [{self.code]}"
