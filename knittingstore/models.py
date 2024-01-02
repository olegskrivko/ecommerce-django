from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pattern_pdf = models.FileField(upload_to='pattern_pdfs/', null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Men'),
        ('W', 'Women'),
        ('U', 'Unisex'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    AGE_CHOICES = [
        ('C', 'Children'),
        ('T', 'Teenagers'),
        ('A', 'Adults'),
        ('S', 'Seniors'),
    ]
    age_group = models.CharField(max_length=1, choices=AGE_CHOICES, default='A')
    DIFFICULTY_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('E', 'Expert'),
    ]
    difficulty_level = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default='B')
    TYPE_CHOICES = [
        ('H', 'Hat'),
        ('S', 'Scarf'),
        ('C', 'Coat'),
        ('SW', 'Sweater'),
        ('O', 'Other'),
        # Add other types as needed
    ]
    product_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='O')

    def __str__(self):
        return self.name
    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.product.name} - {self.name}"
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in Cart {self.cart.id}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)  # Status of the order (pending, completed, etc.)

    def __str__(self):
        return f"Order {self.id} for {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in Order {self.order.id}"