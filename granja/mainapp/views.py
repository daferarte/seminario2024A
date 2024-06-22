from django.shortcuts import render
from products.models import categories

# Create your views here.

def index(request):
    
    categori = categories.objects.all()
    return render(request, 'mainapp/index.html',{
        'title':'Home',
        'categories':categori
    })