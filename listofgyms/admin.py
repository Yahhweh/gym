from django.contrib import admin
from .models import  Gym, WorkingTime


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):

    fields = ['title', 'slug', 'description' , 'location', 'working_time', 'condition', 'image','price', 'longitude' , 'latitude']
    readonly_fields = ('longitude', 'latitude', 'description', 'price')
    prepopulated_fields = {'slug':('title',)}


@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
    fields = ['start_time', 'end_time']
