from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

import uuid
from random import choice
from string import lowercase

from .managers import ProfileManager


def user_image_upload(instance, filename):
    return "profile_images/user%s" % (filename)

ADMIN = "1"
CUSTOMER = "2"
DELIVERY = "3"

USER_ROLE_CHOICES = [
    (ADMIN, "Admin"),
    (CUSTOMER, "Customer/User"),
    (DELIVERY, "Delivery Boy")
]


class Profile(AbstractBaseUser, PermissionsMixin):
    """
    user model containing user's info
    as name/email/username/address
    """
    name = models.CharField(_("Your Name"), max_length=120)
    email = models.EmailField(_("Email"), max_length=70, unique=True)
    username = models.CharField(_("Profilename"), max_length=32, unique=True)
    contact_no = models.CharField(_("Contact Number"), max_length=15, validators=[
        RegexValidator(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'),
        MinLengthValidator(6),
        MaxLengthValidator(15),
        ])
    image = models.FileField(_("Image"), default="user-default.png", upload_to=user_image_upload)
    about = models.TextField(_("About"), blank=True, null=True)
    address = models.TextField(_("Address"))
    city = models.CharField(_("City"), max_length=40, default='Gurgaon')
    state = models.CharField(_("State"), max_length=40, default='Haryana')
    country = models.CharField(_("Country"), max_length=40, default='IN')
    zipcode = models.IntegerField(_("Zip Code"), default=122001)
    facebook_profiile = models.URLField(_("Facebook Profile"), blank=True, null=True)
    twitter_profile = models.URLField(_("Twitter Profile"), blank=True, null=True)
    role = models.CharField(
        _("Profile Role"), max_length=1, choices=USER_ROLE_CHOICES, default=2)
    email_alerts = models.BooleanField(_("Email Alerts"), default=False)
    sms_alerts = models.BooleanField(_("SMS Alerts"), default=False)
    is_staff = models.BooleanField(
        _("Staff Status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."))

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_("Designates whether this user should be treated as "
                    "active. Unselect this instead of deleting accounts."))
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    uuid = models.UUIDField(_("Profile Unique ID"), default=uuid.uuid4, editable=False)
    created = models.DateTimeField(_("Created On"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated On"), auto_now=True)
    delete = models.BooleanField(_("Delete"), default=False)

    objects = ProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        app_label = "accounts"

    def __unicode__(self):
        return "%s" % (self.email)

    def save(self, *args, **kwargs):
        """
        ensure instance has usable password when created &
        add username by default when saving user
        """
        if self.pk is None:
            name = "_".join(str(self.name).split()).replace(".", "_")
            self.username = name.lower() + '_' + ''.join([choice(lowercase) for i in xrange(3)])
        if not self.pk and self.has_usable_password() is False:
            self.set_password(self.password)

        super(Profile, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        return user's full name i.e. first_name and last_name
        """
        return "%s" % (self.name)

    def get_short_name(self):
        return "%s" % (self.name)
