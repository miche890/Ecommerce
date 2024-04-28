def total_cart(request):
    cart_total = 0
    if request.user.is_authenticated:
        if request.session.get('cart'):
            for key, value in request.session['cart'].items():
                cart_total += float(value['total'])

    return {'total_cart': cart_total}


def products_cart(request):
    products = []
    if request.user.is_authenticated:
        if request.session.get('cart'):
            for key, value in request.session['cart'].items():
                products.append(value)

    total_products_cart = len(products)
    return {'products_cart': products, 'total_products_cart': total_products_cart}

