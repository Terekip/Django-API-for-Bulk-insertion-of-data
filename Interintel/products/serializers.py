from rest_framework import serializers
from .models import Product, ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields= ['id','sku','name','price','details']

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields= ['id','name','image','variants']
    