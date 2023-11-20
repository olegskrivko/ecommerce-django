from django.urls import path
from django.views.generic.base import RedirectView
from .views import HomeView, AboutView, CheckoutView, CartView, RemoveFromCartView, AddToCartView, CheckoutView, ContactView
from . import views

app_name = "knittingstore"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    
    path('categories/<slug:category_slug>/', RedirectView.as_view(pattern_name='knittingstore:product-list'), name='category-redirect'),
    path('categories/<slug:category_slug>/products/', views.ProductListView.as_view(), name='product-list'),

    path('categories/<slug:category_slug>/products/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/<int:product_id>/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('contact/', views.ContactView.as_view(), name='contact'),
] 

    
    # path('categories/<slug:category_slug>/', views.CategoryDetailView.as_view(), name='category-detail'),
    # path('categories/<slug:category_slug>/products/', views.ProductListView.as_view(), name='product-list'),
    # path('categories/<slug:category_slug>/', RedirectView.as_view(pattern_name='knittingstore:category-detail'), name='category-redirect'),
    # path('categories/<slug:category_slug>/', views.CategoryDetailView.as_view(), name='category-detail'),