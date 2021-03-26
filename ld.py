phones = ['iPhone Xs', 'Samsung 10Pro', 'Mi 8 Basic']

product = {
    "name": "iPhone XS",
    "stock": 6,
    "price": 65231.2,
    'recommend': phones,
}

print(product["recommend"])

product['recommend'].append('Iphone 10 Pro Max')

print(product["recommend"])