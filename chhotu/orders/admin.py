from django.contrib import admin

from .models import Cart, Order

models = [Cart, Order]

admin.site.register(models)
