from django.contrib import admin

from .models import Feedback, ProductFeedback, ProductOrderTrack

models = [Feedback, ProductFeedback, ProductOrderTrack]

admin.site.register(models)
