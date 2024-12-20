from django.shortcuts import render,HttpResponseRedirect
from .models import Cart,CartItem,Product,Order,OrderItem
from .forms import OrderForm
import uuid
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from superpet.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy

# from products.models import Product
# Create your views here.

@login_required(login_url="/login") #if not logged in then directly redirecting to login page.
def add_to_cart(request,productId):
    print(productId)
    print(request.user)
    currentUser = request.user
    cart_obj,created = Cart.objects.get_or_create(user = currentUser)
    request.session["cart_id"] = cart_obj.id # creating a session for cart object by storing cart_id in the session
    cartitem,created = CartItem.objects.get_or_create(cart = cart_obj,products = Product.customManager.get(id = productId))
    quantity = int(request.GET.get("quantity")) #type cast in string 

    if created:
        cartitem.quantity = quantity
    else:
        cartitem.quantity += quantity 
    
    cartitem.save() #we are connected with the object
    return HttpResponseRedirect("/products")    
    
@login_required(login_url="/login")
def display_cart(request):
    currentUser = request.user
    cart = Cart.objects.get(user=currentUser)
    cartitems = cart.cartitem_set.all()
    total = 0
    for cartitem in cartitems:
        total += cartitem.quantity * cartitem.products.product_price
    return render(request,"cart.html",{"cartitems": cartitems,"total":total})

@login_required(login_url="/login")
def update_cart(request,cartitemId):
    cartitem = CartItem.objects.get(id = cartitemId)
    cartitem.quantity = request.GET.get("quantity")
    cartitem.save()
    return HttpResponseRedirect("/cart")

#@login_required(login_url="/login")
@login_required(login_url=reverse_lazy("login"))
def delete_cartitem(request,cartitemId):
    cartitem =CartItem.objects.get(id = cartitemId)
    print("=============================reverse==================================")
    print(reverse("cart"))
    cartitem.delete()
    return HttpResponseRedirect(reverse("cart"))
    #return HttpResponseRedirect("/cart")    

@login_required(login_url="/login")
def checkout(request):
    if request.method == 'GET':
        form = OrderForm()
        print(request.session.get("cart_id")) # receiving the cart_id
        return render(request,"checkout.html",{"form":form})
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            order = Order.objects.create(orderid = uuid.uuid4().hex,
                                 user = request.user,
                                 address_line_1= form.cleaned_data["address_line_1"],
                                 address_line_2 = form.cleaned_data["address_line_2"],
                                 city = form.cleaned_data["city"],
                                 state = form.cleaned_data["state"],
                                 pincode = form.cleaned_data["pincode"],
                                 phone_number = form.cleaned_data["phone_number"]) 
            cart_id = request.session.get("cart_id")
            cart = Cart.objects.get(id=cart_id)
            cartitems = cart.cartitem_set.all()

            for cartitem in cartitems:
                OrderItem.objects.create(order = order,quantity = cartitem.quantity, products = cartitem.products)
        return HttpResponseRedirect("/cart/payment/"+order.orderid)
    
@login_required(login_url="/login")
def payment(request,orderId):
    order = Order.objects.get(orderid = orderId)
    orderitems = order.orderitem_set.all()
    total = 0
    for orderitem in orderitems:
        total += orderitem.quantity*orderitem.products.product_price
    client = razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3", "LVkt6Cs9VskcAarHG1ryJNdr"))
    data = {"amount": total*100, "currency": "INR", "receipt": orderId}

    payment = client.order.create(data=data)
    return render(request,"payment.html",{"payment":payment})

@csrf_exempt
def payment_success(request,orderId):
    razorpay_response = {
        "razorpay_payment_id":request.POST.get("razorpay_payment_id"),
        "razorpay_order_id":request.POST.get("razorpay_order_id"),
        "razorpay_signature":request.POST.get("razorpay_signature"),
    }
    client=razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3","LVkt6Cs9VskcAarHG1ryJNdr"))
    payment_check=client.utility.verify_payment_signature(razorpay_response)
    if payment_check:
        print("order is paid")
        order = Order.objects.get(orderid=orderId)
        order.paid = True
        order.save()
        send_mail(f"[{order.orderid} placed]",
                  "Order placed successfully.",
                  EMAIL_HOST_USER,
                  ["artilachure@gmail.com","shankkarpal46@gmail.com","tgorivale2@gmailcom"],fail_silently=False)
    return render(request,"success.html")