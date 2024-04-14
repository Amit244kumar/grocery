"""
URL configuration for grocery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from GR.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('shop/',shop),
    path('about/',about),
    path('login/',login),
    path('sign_up/',sign_up),
    path('wishlist/',wishlist), 
    path('create-account/',createAccount),
    path('valiating-user/',validating_user),
    path('profile/',profile),
    path('logout/',logout),
    path('addToCart',addToCart),
    path('contact/',contact),
    path('addProductToCart/',add_product_to_cart),
    path('deleteProduct/',delete_product),
    path('quary/',quary),
    path('forgetPassword/',forgetPassword),
]
