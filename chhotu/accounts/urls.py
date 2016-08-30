from django.conf.urls import url
from accounts import apis, views

urlpatterns = [
    url(r'^register/$', apis.Register.as_view(), name="register"),
    url(r'^login/$', apis.Login.as_view(), name="login"),
    url(r'^logout/$', apis.LogOut.as_view(), name='logout'),
]
