def my_discount(price, discount):
    new_discount = discount / 100
    discount_price = price * new_discount
    return price - discount_price
print(my_discount(150, 15))
