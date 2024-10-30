from django.shortcuts import render,HttpResponseRedirect

# Create your views here.

def add_to_cart(request,productId):
    print(productId)
    print(request.user)
    currentUser = request.user
    return HttpResponseRedirect("/products")

def display_cart(request):
    return render(request,"cart.html")

