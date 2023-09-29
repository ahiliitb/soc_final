from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login.html')
    context = {
                "var": request.user.username
            }
    return render(request, 'index.html', context)
    # return HttpResponse('Hello my name is Ahil Khan')

def about(request):
    context = {
                "var": request.user.username
            }
    return render(request, 'about.html', context)
    # return HttpResponse('Hello about section')

def mylogin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                "var": request.user.username
            }
            return render(request, 'index.html', context)


    return render(request, 'login.html')

def mylogout(request):
    logout(request)

    return render(request, 'login.html')



def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username = username, email = email, password = password)
        user.first_name = name
        user.save()
        return render(request, 'login.html')
    return render(request, 'signup.html')
    # return HttpResponse('Hello about section')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mess = request.POST.get('message')
        contact = Contact(name = name, email = email, phone = phone, mess = mess, date = datetime.today())
        contact.save()
    
    context = {
                "var": request.user.username
            }
    return render(request, 'contact.html', context)
    # return HttpResponse('Hello contact section')

def product(request):
    context = {
                "var": request.user.username
            }
    return render(request, 'product.html', context)

def product1(request):
    context = {
                "var": request.user.username
            }
    return render(request, 'product1.html', context)

def product2(request):
    context = {
                "var": request.user.username
            }
    return render(request, 'product2.html', context)

def product3(request):
    context = {
                "var": request.user.username
            }
    return render(request, 'product3.html', context)

def product4(request):
    context = {
                "var": request.user.username
            }
    return render(request, 'product4.html', context)

def product5(request):
    context = {
                "var": request.user.username
            }
    return render(request, 'product5.html', context)

