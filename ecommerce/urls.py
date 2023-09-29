"""
URL configuration for ecommerce project.

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
from django.urls import path, include

admin.site.site_header = "Welcome to login page"
admin.site.site_title = "Welcome to admin portal"
admin.site.index_title = "Welcome to admin portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about.html', include('home.urls')),
    path('index.html', include('home.urls')),
    path('login.html', include('home.urls')),
    path('signup.html', include('home.urls')),
    path('logout', include('home.urls')),
    path('product.html', include('home.urls')),
    path('product1.html', include('home.urls')),
    path('product2.html', include('home.urls')),
    path('product3.html', include('home.urls')),
    path('product4.html', include('home.urls')),
    path('product5.html', include('home.urls')),
    path('contact.html', include('home.urls'))
]
