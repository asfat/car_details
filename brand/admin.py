from django.contrib import admin
from . import models
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('brandName',)}
    list_display=['brandName','slug']
admin.site.register(models.CarBrand,BrandAdmin)