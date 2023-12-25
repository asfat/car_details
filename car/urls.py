from django.urls import path,include
from . import views
urlpatterns = [
    path('details/<int:id>/',views.CarDetailsView.as_view(),name='carDetails'),
    path('buy/<int:id>/',views.buy_car,name='carDetails2'),
    
]