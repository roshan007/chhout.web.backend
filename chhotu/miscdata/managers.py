
from django.db.models.query import QuerySet
from django.db import models

from .mixins import FeedbackMixin, ProductFeedbackMixin, ProductOrderTrackMixin


class FeedbackQuerySet(QuerySet, FeedbackMixin):
    pass


class FeedbackManager(models.Manager, FeedbackMixin):

    def get_queryset(self):
        return FeedbackQuerySet(self.model, using=self._db).filter(delete=False)


class ProductFeedbackQuerySet(QuerySet, ProductFeedbackMixin):
    pass


class ProductFeedbackManager(models.Manager, ProductFeedbackMixin):

    def get_queryset(self):
        return ProductFeedbackQuerySet(self.model, using=self._db).filter(delete=False)


class ProductOrderTrackQuerySet(QuerySet, ProductOrderTrackMixin):
    pass


class ProductOrderTrackManager(models.Manager, ProductOrderTrackMixin):

    def get_queryset(self):
        return ProductOrderTrackQuerySet(self.model, using=self._db).filter(delete=False)
