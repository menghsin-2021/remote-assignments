def avg(data):
    products = data['products']
    product_price_list = [product['price'] for product in products]
    product_ave_price = round((sum(product_price_list) / len(product_price_list)), 3)

    return product_ave_price


# test run for avg
print(
    avg({
        "products": [
            {
                "name": "Product 1",
                "price": 100
            },
            {
                "name": "Product 2",
                "price": 700
            },
            {
                "name": "Product 3",
                "price": 300
            }
        ]
    })
)  # 366.667