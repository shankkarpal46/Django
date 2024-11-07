from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.

#Function Based View

def about(request):
    return HttpResponse("About Page")

def home(request):
    return HttpResponse("Home Page")

def services(request):
    return HttpResponse("Services Page")

def contact(request):
    return HttpResponse("Contact Page")

def courses(request):
    return render(request,"courses.html",{})

def requirements(request):
    return render(request,"requirement.html",{})

def data(request):
    return render(request,"data.html",{})

class MyView(View):
    def get(self,request):
        return render(request,"my_view.html")
    
    def post(self,request):
        return render(request,"success.html")
    
def learn_filter(request):
    return render(request,"templates_filters.html",{"data":"Django"})

