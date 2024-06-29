from django.shortcuts import render, redirect
from products.models import categories
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    
    categori = categories.objects.all()
    return render(request, 'mainapp/index.html',{
        'title':'Home',
        'categories':categori
    })
    
def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print (user)
        if (user is not None):
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Usuario o contraseña invalidas')
    
    return render(request, 'mainapp/login.html',{
        'title':'Login'
    })

def logout_user(request):
    logout(request)
    return redirect('index')

def createUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mail = request.POST.get('mail')
        
        user = User(
            username=username,
            password=make_password(password, salt=None, hasher='default'),
            email=mail,
        )
        
        user.save()
        
        messages.success(request, 'Usuario Agregado')
        return redirect('index')
        
        print(username, password, mail)
        
    return render(request, 'mainapp/create-user.html',{
        'title':'Login'
    })