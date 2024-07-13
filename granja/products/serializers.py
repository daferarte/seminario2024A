from rest_framework import serializers
from .models import categories, products


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'
