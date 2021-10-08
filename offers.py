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
        
    def get_discounted_price(self, cart_product_codes: list) -> int:
        """
        Returns the offer amount for the given cart items
        
        :param cart_product_codes list: List of product codes in cart
        """
        total = 0
        product_counts = defaultdict(int)
        for product_code in cart_product_codes:
            product_counts[product_code] += 1
            if product_code in self.product_codes:
                # Product has offer
                if product_counts[product_code] % 2 == 0:
                    # Reduce price by half for every even count of that product
                    total += product.price / 2
                else:
                    total += product.price
            else:
                total += product.price
                
        return total
            
