from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView 
from .models import Category, Product
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from decimal import Decimal
import json
# Create your views here.

class HomeView(TemplateView):
    template_name = "knittingstore/home.html"
    
class AboutView(TemplateView):
    template_name = "knittingstore/about.html"  
    
class ContactView(TemplateView):
    template_name = "knittingstore/contact.html"

class CheckoutView(TemplateView):
    template_name = "knittingstore/checkout.html"

class CategoryListView(ListView):
    model = Category
    template_name = 'knittingstore/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'knittingstore/category_detail.html'
    slug_url_kwarg = 'category_slug'
    context_object_name = 'category'

class ProductListView(ListView):
    model = Product
    template_name = 'knittingstore/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'knittingstore/product_detail.html'
    slug_url_kwarg = 'product_slug'  # This should match the parameter in your URL pattern
    context_object_name = 'product'

class AddToCartView(View):
    def get(self, request, product_id):
        print('product_id' + str(product_id))
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})

        if str(product.id) not in cart:
            cart[str(product.id)] = {
                'id': product.id,
                'name': product.name,
                'price': str(product.price),  # Convert Decimal to string for JSON serialization
                # Other product details as needed
            }

            request.session['cart'] = cart
            return HttpResponseRedirect(reverse('knittingstore:cart'))
        else:
            # Product already in the cart; you might want to redirect or show a message
            return HttpResponseRedirect(reverse('knittingstore:cart'))  # Redirect to the cart page or an appropriate page


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = [cart_item for cart_item in cart.values()]
        return render(request, 'knittingstore/cart.html', {'cart_items': cart_items})

class RemoveFromCartView(View):
    def get(self, request, product_id):
        cart = request.session.get('cart', {})
        if str(product_id) in cart:
            del cart[str(product_id)]
            request.session['cart'] = cart
        
        # Redirect to the cart page after removal
        return HttpResponseRedirect(reverse('knittingstore:cart'))

# class CheckoutView(View):
#     def get(self, request):
#         # Fetch cart data from the session
#         cart = request.session.get('cart', {})
        
#         # Pass the cart data to the template
#         return render(request, 'knittingstore/checkout.html', {'cart_items': cart})
    
class CheckoutView(View):
    def get(self, request):
        cart_items = request.session.get('cart', {})
        
        # Convert 'price' values to floats
        for item in cart_items.values():
            item['price'] = float(item['price']) if isinstance(item['price'], str) else item['price']

        # Calculate the total price based on the prices of items in the cart
        cart_total = sum(item['price'] for item in cart_items.values())
        
        context = {
            'cart_items': cart_items,
            'cart_total': cart_total,
        }
        return render(request, 'knittingstore/checkout.html', context)

    

