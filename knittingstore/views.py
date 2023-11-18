from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView 
from .models import Category, Product
# Create your views here.

class HomeView(TemplateView):
    template_name = "knittingstore/home.html"

#  model = Product
#     template_name = 'knittingstore/product_detail.html'  # Replace with your template
#     context_object_name = 'product'  # Name to access the product in the template

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