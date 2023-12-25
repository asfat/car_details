from django.db import models
from brand.models import CarBrand
from django.contrib.auth.models import User
# Create your models here.
class CarDetails(models.Model):
    carName=models.CharField(max_length=30)
    carDescription=models.TextField(blank=True,null=True)
    carPrice=models.IntegerField()
    carQuantity=models.IntegerField()
    carImg=models.ImageField(upload_to='car/media/upload',blank=True,null=True)
    carBrand=models.ForeignKey(CarBrand,on_delete=models.CASCADE)

    def __str__(self):
        return f' Name:{self.carName}, Quanitty:{self.carQuantity} '
    
class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cars_bought = models.ManyToManyField(CarDetails)

    def __str__(self):
        return f' User: {self.user.username} '

    def add_car(self, car):
        self.cars_bought.add(car)

class Comments(models.Model):
    car=models.ForeignKey(CarDetails,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=20)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'commets by {self.name}'
