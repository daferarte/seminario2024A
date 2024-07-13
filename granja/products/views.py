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

    return render(request, 'products/shop-grid.html', {
        'title': 'Productos',
        'categories': categori,
        'products': product
    })


def productDetail(request, product_id):

    product = get_object_or_404(products, id=product_id)

    return render(request, 'products/shop-details.html', {
        'title': 'Producto',
        'product': product
    })

# apiRes


class Product_APIView_List(APIView):
    def get(self, request, format=None, *args, **kwargs):
        product = products.objects.all()
        serializer = ProductsSerializers(product, many=True)
        return Response(serializer.data)


class Product_APIView(APIView):
    def post(self, request, format=None):
        serializer = ProductsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Product_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return products.objects.get(pk=pk)
        except products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializers(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
