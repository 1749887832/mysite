from django.contrib import admin
from app import models
# Register your models here.

admin.site.register(models.Server)
admin.site.register(models.Case_models)
admin.site.register(models.content)
admin.site.register(models.Step)
