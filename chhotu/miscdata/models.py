from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Profile
from products.models import Product
from .managers import FeedbackManager, ProductFeedbackManager, ProductOrderTrackManager


class Feedback(models.Model):
    """
    model to take feedback from user for the service
    """
    user = models.ForeignKey(Profile, related_name=_("user_feedback"))
    feedback = models.TextField(_("Feedback/Comment"))
    submitted_at = models.DateTimeField(_("Feedback Given At"), auto_now_add=True)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = FeedbackManager()

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")
        app_label = "miscdata"

    def __unicode__(self):
        return "%s" % str(self.user.get_full_name())


class ProductFeedback(models.Model):
    """
    model to save feedback for product
    """
    user = models.ForeignKey(Profile, related_name=_("productfeed_user"))
    product = models.ForeignKey(Product, related_name=_("product_feed"))
    rating = models.IntegerField(_("Product Rating"))
    comment = models.TextField(_("Comment"))

    objects = ProductFeedbackManager()

    class Meta:
        verbose_name = _("ProductFeedback")
        verbose_name_plural = _("ProductFeedbacks")
        app_label = "miscdata"

    def __unicode__(self):
        return "%s" % str(self.user.get_full_name())


class ProductOrderTrack(models.Model):
    """
    model to track which product ordered and successfully delivered and how much
    """
    product = models.ForeignKey(Product, related_name=_("product_track"))
    quantity = models.IntegerField(_("Quantity"))
    ordered_at = models.DateTimeField(_("Ordered At"), auto_now_add=True)

    objects = ProductOrderTrackManager()

    class Meta:
        verbose_name = _("ProductOrderTrack")
        verbose_name_plural = _("ProductOrderTracks")
        app_label = "miscdata"

    def __unicode__(self):
        return "%s" % (self.product.name)
