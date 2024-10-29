from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    category_name = models.CharField(max_length=100,null=False)
    category_slug = AutoSlugField(populate_from = "category_name", unique=True)
    
    def __str__(self):
        return self.category_name

# Create your models here.
#Step 1: Create class which inherits Model class from models package

class ProductCustomerManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()

    def royalCanin(self):
        return super().get_queryset().filter(product_brand='Royal Canin')
    
    def rules(self):
        return super().get_queryset().filter(product_brand='Rules')
    

class Product(models.Model):
    product_name = models.CharField(max_length = 100, null = False)
    product_description = models.TextField(default ="product description")
    product_price = models.PositiveIntegerField(default=0)
    product_image = models.ImageField(upload_to="products/")
    product_brand = models.CharField(max_length= 100, default="superpet")

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    
    
    def __str__(self):
        return self.product_name

    riya = models.Manager()
    customManager = ProductCustomerManager()

# class Category():
#     category_title = models.CharField(max_length=100, null=False)
    
