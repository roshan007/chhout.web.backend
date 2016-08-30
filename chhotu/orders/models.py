from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from products.models import Product
from accounts.models import Profile
from .managers import CartManager, OrderManager


CONFIRMED = "1"
INPROGRESS = "2"
DELIVERED = "3"
CANCELLED = "4"

ORDER_DELIVERY_STATUS = [
    (CONFIRMED, "Order Confirmed"),
    (INPROGRESS, "In Progress"),
    (DELIVERED, "Order Delivered"),
    (CANCELLED, "Order Cancelled")
]


class Cart(models.Model):
    """
    model to store cart data entry
    """
    product = models.ForeignKey(Product, related_name=_("product_cart"))
    quantity = models.IntegerField(_("product Quantity"))
    amount = models.DecimalField(_("Total Amount"), max_digits=6, decimal_places=2)
    user = models.ForeignKey(Profile, related_name=_("order_by"), blank=True, null=True)
    pid = models.CharField(_("Cart Session Product ID"), max_length=90)
    uid = models.CharField(_("Cart Session unique ID"), max_length=90)
    added_at = models.DateTimeField(_("Added Datetime"), auto_now_add=True)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = CartManager()

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")
        app_label = "orders"

    def __unicode__(self):
        return "%s" % str(self.product.name)


class Order(models.Model):
    """
    models to store final order data
    """
    product = models.ForeignKey(Product, related_name=_("orders"))
    quantity = models.IntegerField(_("Product Quantity"))
    amount = models.DecimalField(_("Total Amount"), max_digits=6, decimal_places=2)
    delivery_status = models.CharField(_("Delivery Status"), max_length=1, default="1", choices=ORDER_DELIVERY_STATUS)
    user = models.ForeignKey(Profile, related_name=_("user_ordered"))
    ordered_at = models.DateTimeField(_("Order Placed At"), auto_now_add=True)
    delivery_at = models.DateTimeField(_("Order Delivery At"))
    delete = models.BooleanField(_("Delete"), default=False)

    objects = OrderManager()

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        app_label = "orders"

    def __unicode__(self):
        return "%s" % str(self.product.name)
