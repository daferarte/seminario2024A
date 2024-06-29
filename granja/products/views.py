from django.shortcuts import render, get_object_or_404
from .models import categories, products

# Create your views here.
def listProducts(request):
    
    categori = categories.objects.all()
    product = products.objects.all()
    
    return render(request, 'products/shop-grid.html',{
        'title':'Productos',
        'categories':categori,
        'products':product
    })
    
def productDetail(request, product_id):
    
    product = get_object_or_404(products, id=product_id)
    
    return render(request, 'products/shop-details.html',{
        'title':'Producto',
        'product':product
    })