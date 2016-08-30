from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

import datetime
import uuid


class RegisterView(TemplateView):
    """
    view to render register template
    """
    template_name = "accounts/register.html"


class LoginView(TemplateView):
    """
    view to render login template
    """
    template_name = "accounts/login.html"


class HomeView(TemplateView):
    """
    landing page/index page views
    """
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        _urcpid = uuid.uuid4()
        _gpduid = uuid.uuid4()
        max_age = 24 * 60 * 60
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response = render(request, self.template_name)
        if 'urcpid' not in self.request.META and 'gpduid' not in self.request.META:
            response.set_cookie('urcpid', _urcpid, max_age=max_age, expires=expires)
            response.set_cookie('gpduid', _gpduid, max_age=max_age, expires=expires)
        return response


class CartView(TemplateView):
    """
    cart template view
    """
    template_name = "home/cart.html"


class AddressView(TemplateView):
    """
    view to render address template for user detail and update its details
    """
    template_name = "home/address.html"


class OrderReview(TemplateView):
    """
    order review and submit order
    """
    template_name = "home/order-review.html"


class OrderSuccessView(TemplateView):
    """
    view to render success template
    """
    template_name = "home/order-success.html"
