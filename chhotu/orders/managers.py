
from django.db.models.query import QuerySet
from django.db import models

from .mixins import CartMixin, OrderMixin


class CartQuerySet(QuerySet, CartMixin):
    pass


class CartManager(models.Manager, CartMixin):

    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db).filter(delete=False)


class OrderQuerySet(QuerySet, OrderMixin):
    pass


class OrderManager(models.Manager, OrderMixin):

    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db).filter(delete=False)
