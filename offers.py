from abc import ABC, abstractmethod
from collections import defaultdict

class Offer(ABC):
    """
    Base offer class
    """
 
    @abstractmethod
    def get_discounted_price(self):
        pass

    
class HalfPriceForSecond(Offer):
    """
    Offer Implementation for buy one get second at half price offers
    """
    
    def __init__(self, product_codes: list):
        """
        :param product_code list: Product codes for which the buy one get the second at half price exists
        """
        self.product_codes = set(product_codes)
        
    def get_discounted_price(self, cart_products: list) -> int:
        """
        Returns the offer amount for the given cart items
        
        :param cart_products list: List of cart products (< class 'product.Product'>)
        """
        total = 0
        product_counts = defaultdict(int)
        for product in cart_products:
            product_counts[product.code] += 1
            if product.code in self.product_codes:
                # Product has offer
                if product_counts[product.code] % 2 == 0:
                    # Reduce price by half for every even count of that product
                    total += product.price / 2
                else:
                    total += product.price
            else:
                total += product.price
                
        return total
            
