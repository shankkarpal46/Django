"""
URL configuration for learnDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about-page/',views.about),
    path('services-page/',views.services),
    path('contact-page/',views.contact),
    path('courses/',views.courses),
    path('require/',views.requirements),
    path('data/',views.data),
    path('class-based-view/',views.MyView.as_view(),name="class-based-view"),
    path('template-filters/',views.learn_filter,name="template-filter"),
]
