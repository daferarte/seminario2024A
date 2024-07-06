from django.urls import path
from .views import listProducts, productDetail, Product_APIView_List

urlpatterns = [
    path('productos/', listProducts, name="productos"),
    path('productos/<int:product_id>', productDetail, name="producto"),
    path('v1/prod', Product_APIView_List.as_view())
]
