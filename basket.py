from product import Product
from helpers import DeliveryPriceHelper
from offers import Offer


class Basket:
    """
    Basket class for shopping products
    """
    
    def __init__(
        self, 
        product_list: list, 
        delivery_price_helper: DeliveryPriceHelper,
        offer: Offer
    ):
        self.product_catalogue = {p.code: p for p in product_list}
        self.delivery_price_helper = delivery_price_helper
        self.offer = offer
        self.cart = []
        
    @property
    def total_cart_amount(self):
        """
        Returns total cart amount including offers, but excluding delivery price
        """
        return self.offer.get_discounted_price(self.cart)    
    
    def add(self, product_code: str) -> None:
        """
        Add a product to the basket
        
        :param product_code str: Code of the product to be added
        """
        self.cart.append(
            self.product_catalogue[product_code]
        )
    
    def total(self) -> int:
        """
        Get the total amount to be paid for the items added
        
        :returns int: total amount to be paid including the delivery price
        """
        return self.total_cart_amount + \
               self.delivery_price_helper.get_delivery_price(self.total_cart_amount)
    
    
    def clear(self):
        """
        Reset the cart to empty
        """
        self.cart = []
