from product import Product
from helpers import AmountDeliveryPriceHelper
from offers import HalfPriceForSecond

rw = Product('R01', 'Red Widget', 32.95)
gw = Product('G01', 'Green Widget', 24.95)
bw = Product('B01', 'Blue Widget', 7.95)


products = [rw, gw, bw]

offer = HalfPriceForSecond([rw.code])
delivery_p_h = AmountDeliveryPriceHelper({
    0: 4.95,
    50: 2.95,
    90: 0
})


basket = Basket(
    product_list=products, 
    offer=offer,
    delivery_price_helper=delivery_p_h
)

## Check for B01, G01
basket.add('B01')
basket.add('G01')
assert round(basket.total(), 2) == 37.85
basket.clear()

## Check for R01, R01
basket.add('R01')
basket.add('R01')
assert round(basket.total(), 2) == 54.37
print(basket.total())
basket.clear()

## Check for R01, G01
basket.add('R01')
basket.add('G01')
print(basket.total())
assert round(basket.total(), 2) == 60.85
basket.clear()

## Check for B01, B01, R01, R01, R01
basket.add('B01')
basket.add('B01')
basket.add('R01')
basket.add('R01')
basket.add('R01')
print(basket.total())
assert round(basket.total(), 2) == 98.27
basket.clear()
