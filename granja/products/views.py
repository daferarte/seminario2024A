from django.shortcuts import render, get_object_or_404
from .models import categories, products
# inclusion de api
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductsSerializers, CategoriesSerializers

# Create your views here.
# monolito
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

# apiRest
class Product_APIView_List(APIView):
    def get (self, request, format=None, *args, **kwargs):
        product = products.objects.all()
        serializer = ProductsSerializers(product, many=True)
        return Response(serializer.data)