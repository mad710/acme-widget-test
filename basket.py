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
        self.product_catalogue = {p.code: p for p in product_catalogue}
        self.delivery_price_helper = delivery_price_helper
        self.offer = offer
        self.cart = []
        
    @property
    def total_cart_amount(self):
        return self.offer.get_discounted_price(self.cart)    
    
    def add(self, product_code: str) -> None:
        self.cart.append(product_code)
    
    def total(self) -> int:
        return self.delivery_price_helper(self.total_cart_amount)
