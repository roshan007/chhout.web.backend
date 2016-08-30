from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name="registration_view"),
    url(r'^login/$', views.LoginView.as_view(), name="login_view"),

    url(r'^$', views.HomeView.as_view(), name="home_view"),
    url(r'^cart/$', views.CartView.as_view(), name="cart_view"),
    url(r'^address/$', views.AddressView.as_view(), name="address_view"),
    url(r'^order-review/$', views.OrderReview.as_view(), name="order_review"),
    url(r'^order-success/$', views.OrderSuccessView.as_view(), name="order_success_view")
]
