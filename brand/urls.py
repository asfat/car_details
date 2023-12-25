from django.urls import path,include
from . import views
urlpatterns = [
    path('<slug:brand_slug>/', views.home, name='home_brand'),
]