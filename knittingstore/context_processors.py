from .models import Category

def categories_processor(request):
    categories = Category.objects.all()  # Fetch all categories
    return {'categories': categories}  # Return as a dictionary

# def cart_items_count(request):
#     cart_items_count = 0
#     if 'cart' in request.session:
#         cart = request.session['cart']
#         print('cart' + str(cart))
#         cart_items_count = sum(item.get('quantity', 0) for item in cart.values())
#     return {'cart_items_count': cart_items_count}

def cart_items_count(request):
    cart_items_count = 0
    if 'cart' in request.session:
        cart = request.session['cart']
        cart_items_count = len(cart)  # Counting the number of items in the cart
    return {'cart_items_count': cart_items_count}