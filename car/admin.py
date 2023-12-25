from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.CarDetails)
admin.site.register(models.UserDetails)
admin.site.register(models.Comments)