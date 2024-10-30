from django.urls import path
from . import views
urlpatterns = [
    #path('',views.products,name = "products"),
    path('',views.ProductListView.as_view(),name = "products"),
    path('Royal-Canin/',views.royalCanin,name = "Royal_Canin"),
    path('Rules/',views.rules,name = "Rules"),
    path('search/',views.search,name = "search"),
    path('<int:pk>/',views.ProductDetailView.as_view(),name ="product-details"),
    path('create-product/',views.ProductCreateView.as_view(),name="create-product"),
    path('update-product/<int:pk>/',views.ProductUpdateView.as_view(),name="product-update"),
    path('delete-product/<int:pk>/',views.ProductDeleteView.as_view(),name="product-delete"),
    path('<slug:slug>/',views.Category_DetailView.as_view(),name="category-detail"),
]

