from django.urls import path
from .views import HomeView
from . import views


app_name = "knittingstore"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:category_slug>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<slug:category_slug>/products/', views.ProductListView.as_view(), name='product-list'),
    path('categories/<slug:category_slug>/products/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product-detail'),
     # Cart and checkout views
    # path('cart/', views.CartView.as_view(), name='cart'),
    # path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    # Add more URL patterns for adding/removing items from the cart, order summary, etc.
] 


