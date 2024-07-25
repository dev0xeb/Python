def product_of_integers(*args):
    product = 1
    for num in args:
        product *= num
    return product
print(product_of_integers(1, 2, 3, 4, 5, 6, 7, 8, 9,))
