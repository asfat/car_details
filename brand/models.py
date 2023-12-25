from django.db import models

# Create your models here.
class CarBrand(models.Model):
    brandName=models.CharField(max_length=25)
    slug=models.SlugField(max_length=100,unique=True,blank=True,null=True)

    def __str__(self):
        return self.brandName
    