from product import Product
from helpers import DeliveryPriceHelper
from offers import Offer


class Basket:
    
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
        return self.offer.get_discounted_price(self.cart)    
    
    def add(self, product_code: str) -> None:
        self.cart.append(
            self.product_catalogue[product_code]
        )
    
    def total(self) -> int:
        return self.total_cart_amount + \
               self.delivery_price_helper.get_delivery_price(self.total_cart_amount)
    
    
    def clear(self):
        self.cart = []
