from django.urls import path
from .views import listProducts, productDetail, Product_APIView_List, Product_APIView, Product_APIView_Detail

urlpatterns = [
    path('productos/', listProducts, name="productos"),
    path('productos/<int:product_id>', productDetail, name="producto"),
    path('v1/prod', Product_APIView_List.as_view()),
    path('v1/prod/add', Product_APIView.as_view()),
    path('v1/prod/<int:pk>', Product_APIView_Detail.as_view()),
]
