from django.conf.urls import url

from orders import apis

urlpatterns = [
    url(r'^cart/$', apis.AddToCart.as_view(), name="api_addtocart"),
]
