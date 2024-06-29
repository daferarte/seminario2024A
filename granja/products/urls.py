from django.urls import path
from .views import listProducts, productDetail

urlpatterns = [
    path('productos/', listProducts, name="productos"),
    path('productos/<int:product_id>', productDetail, name="producto"),
]
