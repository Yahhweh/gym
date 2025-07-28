from django.contrib import admin
from .models import CustomUser, Trainings
from listofgyms.models import Subscription


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    fields = ['gym', 'username', 'quantity', 'start_date', 'end_date']
    readonly_fields = ['start_date', 'end_date']


class TrainingsInline(admin.TabularInline):
    model = Trainings
    fields = ['trainer', 'username', 'quantity','date_of_training']
    readonly_fields = ['trainer','date_of_training']


@admin.register(CustomUser)
class GymUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'image', 'email', 'slug', 'profit', 'role',
                    'is_active', 'location', 'specialization', 'experience_years', 'price')

    fields = ['username', 'first_name', 'last_name', 'image', 'email', 'slug', 'is_active', 'is_staff','profit','role',
              'location', 'specialization', 'experience_years', 'price', 'free']

    prepopulated_fields = {'slug': ('username',)}

    readonly_fields = ('last_login', 'date_joined', 'profit',)

    list_filter = ('is_active', 'is_staff', 'experience_years', 'price')

    search_fields = ('username', 'email', 'first_name', 'last_name', 'location')

    inlines = [SubscriptionInline, TrainingsInline]
