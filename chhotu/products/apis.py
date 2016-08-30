
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductsApi(generics.ListAPIView):
    """
    api to list down products
    """
    model = Product
    serializer_class = ProductSerializer
    queryset = model.objects.all()

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is not None:
            return self.queryset.filter(category__in=list(category.split(',')))
        return self.queryset
