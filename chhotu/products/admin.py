from django.contrib import admin

from .models import Product

models = [Product]

admin.site.register(models)
