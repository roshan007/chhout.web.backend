
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    serializer for product list/create api
    """
    class Meta:
        model = Product
