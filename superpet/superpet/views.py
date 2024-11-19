from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from products.models import Product
from django.contrib.auth.decorators import user_passes_test
def home(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def user_login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password) 
        if user is not None:
            login(request,user)
            print(request.user.first_name)
            return HttpResponseRedirect("/products")
        else:
            return render(request,"login.html",{"message":"Login failed"})
    
def register(request):
    if request.method == 'GET':
        #form = UserCreationForm()
        form = CustomUserCreationForm(request.POST)
        return render(request,"register.html",{"form":form})
    else:
        #form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html",{"form":form})        

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@user_passes_test(lambda u:u.is_superuser,login_url="/admin-portal")
def admin(request):
    return render(request,"admin.html",{"products":Product.customManager.all(),"count":Product.customManager.count()})

def profile(request):
    return render(request,"profile.html")