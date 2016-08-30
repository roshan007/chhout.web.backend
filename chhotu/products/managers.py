
from django.db.models.query import QuerySet
from django.db import models

from .mixins import ProductCategoryMixin, ProductMixin, ProductDiscountMixin, DiscountMixin


class ProductCategoryQuerySet(QuerySet, ProductCategoryMixin):
    pass


class ProductCategoryManager(models.Manager, ProductCategoryMixin):

    def get_queryset(self):
        return ProductCategoryQuerySet(self.model, using=self._db).filter(delete=False)


class ProductQuerySet(QuerySet, ProductMixin):
    pass


class ProductManager(models.Manager, ProductMixin):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db).filter(delete=False)


class ProductDiscountQuerySet(QuerySet, ProductDiscountMixin):
    pass


class ProductDiscountManager(models.Manager, ProductDiscountMixin):

    def get_queryset(self):
        return ProductDiscountQuerySet(self.model, using=self._db).filter(delete=False)


class DiscountQuerySet(QuerySet, DiscountMixin):
    pass


class DiscountManager(models.Manager, DiscountMixin):

    def get_queryset(self):
        return ProductCategoryQuerySet(self.model, using=self._db).filter(delete=False)
