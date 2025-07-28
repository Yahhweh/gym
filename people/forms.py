
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from listofgyms.constants import LOCATIONS, PRODUCT_CHOICES, SPECIALIZATIONS, SPECIALIZATION_RATE
from listofgyms.models import Gym


location_field = Gym._meta.get_field('location')
choices_dict = dict(location_field.choices)
used_locations = Gym.objects.values_list('location', flat=True).distinct()
LOCATION_CHOICES = []
for loc in used_locations:
    if loc in choices_dict:
        LOCATION_CHOICES.append((loc, choices_dict[loc]))


class CustomUserForm(UserCreationForm):
    role = forms.ChoiceField(choices=PRODUCT_CHOICES, required=True)
    specialization = forms.ChoiceField(choices=SPECIALIZATIONS, required=False)
    experience_years = forms.IntegerField(required=False)
    location = forms.ChoiceField(choices=LOCATION_CHOICES, required=False)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'role', 'image', 'specialization',
                  'experience_years', 'password1', 'password2', 'location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        if self.is_bound:
            role = self.data.get('role')
            if role == 'trainer':
                self.fields['specialization'].required = True
                self.fields['experience_years'].required = True
                self.fields['location'].required = True

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')

        if role == 'trainer':
            if not cleaned_data.get('specialization'):
                self.add_error('specialization', 'This field is required for trainers.')

            if not cleaned_data.get('experience_years'):
                self.add_error('experience_years', 'This field is required for trainers.')

            if not cleaned_data.get('location'):
                self.add_error('location', 'This field is required for trainers.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        if user.role == 'client':
            user.specialization = None
            user.experience_years = None
            user.location = None
            user.price = None
        else:
            user.price = self.calculate_hourly_rate()
            pass

        if commit:
            user.save()
        return user


    def calculate_hourly_rate(self):
        base_rate = self.cleaned_data.get('specialization')
        experience = self.cleaned_data.get('experience_years')
        bonus = int(experience) * 0.5
        return int(base_rate) * SPECIALIZATION_RATE[(int(base_rate))] * bonus


