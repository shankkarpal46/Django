from django.shortcuts import render
from .models import Product,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def products(request):
    return render(request,"products.html")

def royalCanin(request):
    products = Product.customManager.royalCanin()
    return render(request,"products.html",{"products": products})

def rules(request):
    products = Product.customManager.rules()
    return render(request,"products.html",{"products":products})

def search(request):
    keyword = request.GET.get("keyword")
    products = Product.customManager.all().filter(product_name__icontains=keyword)
    return render(request,"products.html",{"products":products})


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/productdetail.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.customManager.all()
        context["name"] = "Trupti"
        return context
    
@method_decorator(staff_member_required,name="dispatch")
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = "/products"

@method_decorator(staff_member_required,name="dispatch")
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url ="/products"

@method_decorator(staff_member_required,name="dispatch")
class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products'

class Category_DetailView(DetailView):
    model = Category
    template_name = "category/categorydetail.html"
    slug_field = "category_slug"
    context_object_name = "category_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
