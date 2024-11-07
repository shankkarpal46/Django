from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one relationship
    products = models.ManyToManyField(Product,through = "CartItem")

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default = 0)
    products = models.ForeignKey(Product,on_delete=models.PROTECT)

class Order(models.Model):
    orderid = models.CharField(max_length=100,primary_key = True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address_line_1 = models.CharField(max_length=100,null=False)
    address_line_2 = models.CharField(max_length=100,null=False)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    pincode = models.IntegerField(null=False)
    phone_number = models.BigIntegerField(null=False)



