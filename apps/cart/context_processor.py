def total_cart(request):
    cart_total = 0
    if request.user.is_authenticated:
        if request.session.get('cart'):
            for key, value in request.session['cart'].items():
                cart_total += float(value['total'])

    return {'total_cart': cart_total}
