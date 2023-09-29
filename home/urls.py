from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about.html', views.about, name='about'),
    path('index.html', views.index, name='home2'),
    path('contact.html', views.contact, name='contact'),
    path('signup.html', views.signup, name='signup'),
    path('logout', views.mylogout, name='signup'),
    path('product.html', views.product, name='signup'),
    path('product1.html', views.product1, name='signup'),
    path('product2.html', views.product2, name='signup'),
    path('product3.html', views.product3, name='signup'),
    path('product4.html', views.product4, name='signup'),
    path('product5.html', views.product5, name='signup'),
    path('login.html', views.mylogin, name='mylogin'),
]