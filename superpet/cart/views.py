from django.shortcuts import render,HttpResponseRedirect
from .models import Cart,CartItem,Product,Order
from .forms import OrderForm
import uuid
#from products.models import Product
# Create your views here.

def add_to_cart(request,productId):
    print(productId)
    print(request.user)
    currentUser = request.user
    cart_obj,created = Cart.objects.get_or_create(user = currentUser)
    cartitem,created = CartItem.objects.get_or_create(cart = cart_obj,products = Product.customManager.get(id = productId))
    quantity = int(request.GET.get("quantity")) #type cast in string 

    if created:
        cartitem.quantity = quantity
    else:
        cartitem.quantity += quantity 
    
    cartitem.save() #we are connected with the object
    return HttpResponseRedirect("/products")    
    

def display_cart(request):
    currentUser = request.user
    cart = Cart.objects.get(user=currentUser)
    cartitems = cart.cartitem_set.all()
    total = 0
    for cartitem in cartitems:
        total += cartitem.quantity * cartitem.products.product_price
    return render(request,"cart.html",{"cartitems": cartitems,"total":total})

def update_cart(request,cartitemId):
    cartitem = CartItem.objects.get(id = cartitemId)
    cartitem.quantity = request.GET.get("quantity")
    cartitem.save()
    return HttpResponseRedirect("/cart")

def delete_cartitem(request,cartitemId):
    cartitem =CartItem.objects.get(id = cartitemId)
    cartitem.delete()
    return HttpResponseRedirect("/cart")

def checkout(request):
    if request.method == 'GET':
        form = OrderForm()
        return render(request,"checkout.html",{"form":form})
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            Order.objects.create(orderid = uuid.uuid4().hex,
                                 user = request.user,
                                 address_line_1= form.cleaned_data["address_line_1"],
                                 address_line_2 = form.cleaned_data["address_line_2"],
                                 city = form.cleaned_data["city"],
                                 state = form.cleaned_data["state"],
                                 pincode = form.cleaned_data["pincode"],
                                 phone_number = form.cleaned_data["phone_number"])
        return HttpResponseRedirect("/cart/checkout")
    