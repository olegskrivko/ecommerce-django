from django.urls import path
from django.views.generic.base import RedirectView
from .views import HomeView, AboutView, CategoryListView, ProductListView, ProductDetailView,PaymentView, CheckoutView, CartView, RemoveFromCartView, AddToCartView, ContactView
from . import views

app_name = "knittingstore"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("categories/", CategoryListView.as_view(), name="category-list"),  # Show all categories
    path("categories/<slug:category_slug>/", ProductListView.as_view(), name="product-list"),  # Show products for a specific category
    path("categories/<slug:category_slug>/products/<slug:product_slug>/", ProductDetailView.as_view(), name="product-detail"),  # Show details for a product
    # path('categories/<slug:category_slug>/', RedirectView.as_view(pattern_name='knittingstore:product-list'), name='category-redirect'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/<int:product_id>/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('payment/', PaymentView.as_view(), name='payment'),
    # path('payment-success/', PaymentSuccessView.as_view(), name='payment-success'),
    # path('payment-cancel/', PaymentCancelView.as_view(), name='payment-cancel'),

] 
