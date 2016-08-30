
from django.conf.urls import url
from products import apis


urlpatterns = [
    url(r'^$', apis.ProductsApi.as_view(), name="api_products_list")
]
