
from abc import ABC, abstractmethod
 
class DeliveryPriceHelper(ABC):
    """
    Interface for delivery price helper. 
    Can be extended to have different strategies for deciding delivery price.
    """
 
    @abstractmethod
    def get_delivery_price(self):
        pass


class AmountDeliveryPriceHelper(DeliveryPriceHelper):
    """
    Helper class to return the delivery price based on the amount spent 
    """
    
    def __init__(self, level_prices: dict):
        """
        :param level_prices dict: Dictionary containing delivery prices vs amount spend lower bounds (in dollars)
                                  ex: {
                                      0: 4.95
                                      50: 2.95,
                                      90: 0
                                  }
        """
        self.level_prices = level_prices
        self._sorted_levels = sorted(self.level_prices.keys())
        
        
    def get_delivery_price(self, amount: int) -> int:
        """
        :param amount int: amount for which we need the delivery price
        """
        delivery_price = self.level_prices[0]
        for level in self._sorted_levels:
            if amount < level:
                # Got the delivery price
                break
            # Amount is greater; Go to the next price level
            delivery_price = self.level_prices[level]
            
        return delivery_price
