from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, TemplateView
from django.views.generic import DetailView
from .models import Gym, WorkingTime
from people.models import CustomUser
import time, datetime
from .constants  import LOCATIONS

class GymList(ListView):
    template_name = 'listofgyms/gym_list.html'

    def get_queryset(self):
        return Gym.objects.all()


class GymDetail(DetailView):
    model = Gym
    template_name = 'listofgyms/gym_detail.html'
    context_object_name = 'gym'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        location = self.object.location

        sort_order = self.request.GET.get('sort', 'asc')

        if sort_order == 'desc':
            trainers = CustomUser.objects.filter(
                role='trainer', location=location
            ).order_by('-price')
        else:
            trainers = CustomUser.objects.filter(
                role='trainer', location=location
            ).order_by('price')

        cur_hour = time.localtime().tm_hour
        cur_min = time.localtime().tm_min
        cur_time = datetime.time(cur_hour, cur_min)
        gym = Gym.objects.get(id=self.object.id)
        working_time = gym.working_time
        working_time_start = working_time.start_time
        working_time_end = working_time.end_time
        is_time = working_time_start <= cur_time < working_time_end






        context['trainers'] = trainers
        context['sort_order'] = sort_order
        context['range'] = range(len(CustomUser.objects.all()))
        context['latitude']= self.object.latitude
        context['longitude'] = self.object.longitude
        context['is_time'] = is_time

        return context

