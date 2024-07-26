def gratuity_total(gratuity_rate, subtotal):
    gratuity = (gratuity_rate / 100) * 10
    total = subtotal + gratuity
    return gratuity, total
print(gratuity_total(15, 10))
