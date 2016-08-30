
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from products.models import Product
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    """
    serializer for add to cart api
    """

    def validate(self, attrs):
        view = self.context.get('view')
        attrs['amount'] = int(attrs.get('quantity')) * attrs.get('product').price
        if view.request.user.is_authenticated():
            attrs['user'] = view.request.user
        return attrs

    class Meta:
        model = Cart
        fields = ('product', 'quantity')
