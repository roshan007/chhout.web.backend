from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

from .managers import ProductManager
from .constants import PRODUCT_STATUS_CHOICES, PRODUCT_CATEGORY_CHOICES


def product_logo_upload(instance, filename):
    return "products/%s" % (filename)


class Product(models.Model):
    """
    model to store product details
    """
    name = models.CharField(_("Product Name"), max_length=100)
    logo = models.FileField(_("Product Logo"), upload_to=product_logo_upload)
    price = models.DecimalField(_("Product Price"), max_digits=6, decimal_places=2)
    rating = models.DecimalField(_("Product Rating"), max_digits=2, decimal_places=1, default=0.0)
    availability = models.CharField(_("Product Status"), max_length=1, choices=PRODUCT_STATUS_CHOICES)
    category = models.CharField(_("Product Category"), max_length=3, choices=PRODUCT_CATEGORY_CHOICES)
    uuid = models.UUIDField(_("Product Unique ID"), default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = ProductManager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        app_label = "products"

    def __unicode__(self):
        return "%s" % (self.name)
