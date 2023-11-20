from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView 
from .models import Category, Product
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from decimal import Decimal
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
# for payments
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

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


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductListView(ListView):
    model = Product
    template_name = 'knittingstore/product_list.html'
    context_object_name = 'products'
    paginate_by = 10  # Number of items per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        context['category_slug'] = category_slug

        # Retrieve filter values from the GET request
        age_group = self.request.GET.get('age_group')
        difficulty = self.request.GET.get('difficulty')
        product_type = self.request.GET.get('product_type')
        sort_by_price = self.request.GET.get('sort_by_price')  # Added sorting parameter

        # Apply filters based on parameters
        filtered_products = Product.objects.filter(category__slug=category_slug)
        if age_group:
            filtered_products = filtered_products.filter(age_group=age_group)
        if difficulty:
            filtered_products = filtered_products.filter(difficulty_level=difficulty)
        if product_type:
            filtered_products = filtered_products.filter(product_type=product_type)

        # Apply sorting by price if requested
        if sort_by_price == 'asc':
            filtered_products = filtered_products.order_by('price')
        elif sort_by_price == 'desc':
            filtered_products = filtered_products.order_by('-price')

        # Pagination
        paginator = Paginator(filtered_products, self.paginate_by)
        page_number = self.request.GET.get('page')
        try:
            products = paginator.page(page_number)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products
        return context


# class ProductListView(ListView):
#     model = Product
#     template_name = 'knittingstore/product_list.html'
#     context_object_name = 'products'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category_slug = self.kwargs['category_slug']
#         context['category_slug'] = category_slug

#         # Retrieve filter values from the GET request
#         age_group = self.request.GET.get('age_group')
#         difficulty = self.request.GET.get('difficulty')
#         product_type = self.request.GET.get('product_type')
#         sort_by_price = self.request.GET.get('sort_by_price')  # Added sorting parameter

#         # Apply filters based on parameters
#         filtered_products = Product.objects.filter(category__slug=category_slug)
#         if age_group:
#             filtered_products = filtered_products.filter(age_group=age_group)
#         if difficulty:
#             filtered_products = filtered_products.filter(difficulty_level=difficulty)
#         if product_type:
#             filtered_products = filtered_products.filter(product_type=product_type)

#         # Apply sorting by price if requested
#         if sort_by_price == 'asc':
#             filtered_products = filtered_products.order_by('price')
#         elif sort_by_price == 'desc':
#             filtered_products = filtered_products.order_by('-price')

#         context['products'] = filtered_products
#         return context

#     def get_queryset(self):
#         # This method is not used when filtering in get_context_data
#         return Product.objects.none()  # Return an empty queryset since filtering is done in get_context_data

# class ProductListView(ListView):
#     model = Product
#     template_name = 'knittingstore/product_list.html'
#     context_object_name = 'products'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category_slug = self.kwargs['category_slug']
#         context['category_slug'] = category_slug

#         # Retrieve filter values from the GET request
#         age_group = self.request.GET.get('age_group')
#         difficulty = self.request.GET.get('difficulty')
#         product_type = self.request.GET.get('product_type')

#         # Retrieve the sort parameter from the GET request
#         sort_by_price = self.request.GET.get('sort_by_price')

#         # Filter products based on category_slug
#         filtered_products = Product.objects.filter(category__slug=category_slug)

#         # Apply additional filters if values are provided in the request
#         if age_group:
#             filtered_products = filtered_products.filter(age_group=age_group)
#         if difficulty:
#             filtered_products = filtered_products.filter(difficulty_level=difficulty)
#         if product_type:
#             filtered_products = filtered_products.filter(product_type=product_type)

#         # Apply sorting if requested
#         if sort_by_price == 'asc':
#             filtered_products = filtered_products.order_by('price')
#         elif sort_by_price == 'desc':
#             filtered_products = filtered_products.order_by('-price')

#         context['products'] = filtered_products
#         return context


# class ProductListView(ListView):
#     model = Product
#     template_name = 'knittingstore/product_list.html'
#     context_object_name = 'products'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category_slug = self.kwargs['category_slug']
#         context['category_slug'] = category_slug

#         # Retrieve filter values from the GET request
#         age_group = self.request.GET.get('age_group')
#         difficulty = self.request.GET.get('difficulty')
#         product_type = self.request.GET.get('product_type')

#         # Apply filters if values are provided in the request
#         filtered_products = Product.objects.filter(category__slug=category_slug)
#         if age_group:
#             filtered_products = filtered_products.filter(age_group=age_group)
#         if difficulty:
#             filtered_products = filtered_products.filter(difficulty_level=difficulty)
#         if product_type:
#             filtered_products = filtered_products.filter(product_type=product_type)
            

#         context['products'] = filtered_products
#         return context

#     def get_queryset(self):
#         # This method is not used when filtering in get_context_data
#         return Product.objects.none()  # Return an empty queryset since filtering is done in get_context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'knittingstore/product_detail.html'
    slug_url_kwarg = 'product_slug'  # This should match the parameter in your URL pattern
    context_object_name = 'product'

# class AddToCartView(View):
#     def get(self, request, product_id):
#         product = get_object_or_404(Product, pk=product_id)
#         cart = request.session.get('cart', {})

#         # Increment the quantity if the item is already in the cart
#         if str(product.id) in cart:
#             cart[str(product.id)]['quantity'] = cart[str(product.id)].get('quantity', 0) + 1
#         else:
#             # Add the item to the cart with quantity 1 if it's not already present
#             cart[str(product.id)] = {
#                 'id': product.id,
#                 'name': product.name,
#                 'price': str(product.price),
#                 'quantity': 1,  # Set quantity to 1 for the new item
#             }

#         request.session['cart'] = cart
#         cart_items_count = sum(item.get('quantity', 0) for item in cart.values())
#         print("Cart Items Count:", cart_items_count)

#         return HttpResponseRedirect(reverse('knittingstore:cart'))

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


class PaymentView(View):
    
    def get(self, request):
        
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '100.00',  # Replace with the actual amount
            'currency_code': 'USD',  # Replace with the currency code
            'item_name': 'Product Name',  # Replace with the product name
            'invoice': 'unique-invoice-id',  # Replace with a unique invoice ID
            'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),  # Replace with your IPN URL
            'return_url': request.build_absolute_uri(reverse('payment-success')),
            'cancel_return': request.build_absolute_uri(reverse('payment-cancel')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'payment/payment.html', {'form': form})
    
# class CheckoutView(View):
#     def get(self, request):
#         # Collect order information
#         # Render the checkout template with order details
#         return render(request, 'checkout.html', context)

#     def post(self, request):
#         # Process the checkout form submission
#         # Initiate the payment process (PayPal or other gateway)
#         # Redirect the user to the payment gateway's endpoint
#         return redirect(payment_gateway_url)  # Redirect to the payment gateway

# class PaymentSuccessView(View):
#     def get(self, request):
#         # Handle successful payment callback from the payment gateway
#         # Update order status, confirm payment, etc.
#         return render(request, 'payment_success.html')

# class PaymentCancelView(View):
#     def get(self, request):
#         # Handle canceled payment callback from the payment gateway
#         # Update order status or take necessary action
#         return render(request, 'payment_cancel.html')