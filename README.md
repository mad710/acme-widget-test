# acme-widget-test


## Creating Products


```python
from product import Product

rw = Product('R01', 'Red Widget', 32.95)
gw = Product('G01', 'Green Widget', 24.95)
bw = Product('B01', 'Blue Widget', 7.95)


products = [rw, gw, bw]
```


## Creating the Delivery Price Rules


```python
from helpers import AmountDeliveryPriceHelper

delivery_level_prices = {
    0: 4.95,
    50: 2.95,
    90: 0
}

delivery_price_helper = AmountDeliveryPriceHelper(delivery_level_prices)
```

## Creating an Offer
```python
from offers import HalfPriceForSecond

# Pass the product codes for which HalfPriceForSecond offer has to be applied
hp_offer = HalfPriceForSecond([rw.code])
```


## Creating a basket
```python
from basket import Basket

# Pass the offer and deliver price helper objects
basket = Basket(
    product_list=products, 
    offer=hp_offer,
    delivery_price_helper=delivery_price_helper
)
```

## Adding an item to basket
```python
# Pass the product code of the item to be added
basket.add('B01') # Add Blue Widget

basket.add('G01') # Add Green Widget
```

## Clearing the basket
```python
basket.clear()
```

## Calculating the total amount 
```python
basket.total()
```


Improvements:
- We could update the total amount every time the cart is updated instead of calculating it every time when the total is calculated.
- HalfPriceForSecond offer class could be generalized to accept any factor of price reduction (1/3rd, 1/4th or any percentage like 40% etc)
- Basic functionality of basket.remove(product_code) functionality has to be provided
