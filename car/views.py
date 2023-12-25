from django.shortcuts import render, redirect
from .models import UserDetails, CarDetails, Comments
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import CommentForm
from django.db import transaction

# Create your views here.
# def home(request,id):
#     car=CarDetails.objects.get(pk=id)
#     return render(request,'cardetails.html',{'car':car})
class CarDetailsView(DetailView):
    model = CarDetails
    template_name = 'cardetails.html'
    pk_url_kwarg = 'id'
    context_object_name = 'car'

    def post(self,request,*args,**kwargs):
        Comment_form=CommentForm(data=self.request.POST)
        car=self.get_object()
        if Comment_form.is_valid():
            new_comment=Comment_form.save(commit=False)
            new_comment.car=car
            new_comment.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comments_form= CommentForm()
        context['comments']=comments
        context['comments_form']=comments_form
        return context

@login_required
def buy_car(request, id):
    user = request.user  
    car = CarDetails.objects.get(pk=id)   
    user_details = UserDetails.objects.filter(user=user, cars_bought=car)

    if user_details is None:
        user_details = UserDetails.objects.get(user=user)
        user_details.add_car(car)
        car.carQuantity -= 1
        car.save()

    return redirect('carDetails2', id=car.id)
    
