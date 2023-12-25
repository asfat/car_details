"""
URL configuration for car_selling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='root'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('register/',views.registerView.as_view(),name='register'),
    path('login/',views.UsrLoginView.as_view(),name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('brand/',include('brand.urls')),
    path('car/',include('car.urls')),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)