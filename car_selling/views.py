from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from brand.models import CarBrand
from car import models
from django.contrib.auth.decorators import login_required
from car.models import UserDetails

def home(request,brand_slug=None):
    categories= CarBrand.objects.all()
    allCar=models.CarDetails.objects.all()
    return render(request,'brand.html',{'categories':categories,'allCar':allCar})

class registerView(CreateView):
    model = User
    form_class=RegisterForm
    template_name='login.html'
    success_url = reverse_lazy('root')	

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['text']= 'This is Register Form Page'
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class UsrLoginView(LoginView):
    template_name='login.html'

    def form_valid(self, form):
        messages.success(self.request,'Logged In Successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,'Loggedin Info is Incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = 'Logged In Form'
        return context
    def get_success_url(self):
        return reverse_lazy('root')
    
def user_logout(request):
    logout(request)
    return redirect('root')

@login_required
def profile(request):
    details= UserDetails.objects.get(user=request.user)
    return render(request,'profile.html',{'details':details})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = ChangeUserData(instance = request.user)
    return render(request, 'login.html', {'form' : profile_form})
