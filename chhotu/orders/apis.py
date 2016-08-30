
from rest_framework import generics, response, status

from .models import Cart
from .serializers import CartSerializer


class AddToCart(generics.ListCreateAPIView):
    """
    api to support adding products to cart
    """
    model = Cart
    serializer_class = CartSerializer

    def get_queryset(self):
        print self.request.META
        if self.request.user.is_authenticated():
            return self.model.objects.filter(user=self.request.user)
        else:
            return self.model.objects.filter(pid=self.request.META.get('urcpid', None), uid=self.request.META.get('gpduid'))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.validated_data['pid'] = self.request.META.get('urcpid', None)
        serializer.validated_data['uid'] = self.request.META.get('gpduid', None)
        serializer.save()
