def discounted(price, discount, max_discount=40):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Дохуя скидка не думаєш?')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

product = {
    'name': 'Samsung S10',
    'stock': 8,
    'price': 50000.0,
    'discount': 100,
}

product['with_discount'] = discounted(product['price'], product['discount'], max_discount=80)

print(product)

discounted(100, 5)