from django.shortcuts import render
from .models import CarBrand
from car import models
# Create your views here.
def home(request,brand_slug=None):
    categories= CarBrand.objects.all()
    allCar=models.CarDetails.objects.all()
    if brand_slug is not None:
        category=CarBrand.objects.get(slug=brand_slug)
        allCar=models.CarDetails.objects.filter(carBrand=category)

    return render(request,'brand.html',{'categories':categories,'allCar':allCar})