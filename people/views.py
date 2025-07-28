from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views import  View
from .models import CustomUser, Trainings
from django.views.generic import ListView, DetailView
import  time
from listofgyms.models import WorkingTime
from django.contrib.auth.decorators import login_required
from listofgyms.models import Subscription, Gym


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('listofgyms:gym_list')
    else:
        form = CustomUserForm()

    return render(request, 'registration/register.html', {'form': form})


class ProfileView(View):
    login_url = '/login/'
    redirect_field_name = 'next'
    def get(self, request):
        user = request.user
        gyms = Gym.objects.all()
        subscriptions = Subscription.objects.filter(username = user)
        trainings = Trainings.objects.filter(username=user)


        if user.is_trainer():
            return render( request, 'customer/profile_trainer.html', {'user':user,
                                                                      'subscriptions':subscriptions,
                                                                      'gyms':gyms,
                                                                      'trainings':trainings})
        else:
            return render(request, 'customer/profile_user.html', {'user':user,
                                                                  'subscriptions':subscriptions,
                                                                  'gyms':gyms,
                                                                  'trainings':trainings
                                                                  })


class DetailTrainers(DetailView):
    login_url = '/login/'
    redirect_field_name = 'next'
    model = CustomUser
    template_name = 'customer/trainers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_gym'] = WorkingTime.objects.all()
        return context


    def post(self, *args, **kwargs):
        trainer = self.get_object()
        trainer.free = False
        trainer.save()
        seconds = time.time()
        local_time = time.ctime(seconds)

        return HttpResponse(f'you`ve been booked a lesson in {local_time}. ')






