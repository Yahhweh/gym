from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from listofgyms.constants import LOCATIONS, SPECIALIZATIONS, PRODUCT_CHOICES
import datetime

class CustomUser(AbstractUser):
    LOCATION_CHOICES = []
    for i in LOCATIONS:
        LOCATION_CHOICES.append((i[0], i[1]))


    slug = models.SlugField(max_length=50, unique=True, blank=True)
    role = models.CharField(max_length=10, choices=PRODUCT_CHOICES, default='client')
    image = models.ImageField(upload_to='images/', blank=True)


    specialization = models.IntegerField(choices=SPECIALIZATIONS, null=True, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    location = models.IntegerField(choices=LOCATION_CHOICES,null=True, blank=True )
    free = models.BooleanField(default=True)
    profit = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.username}-{self.role}")
            slug = base_slug
            counter = 1
            while CustomUser.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def is_trainer(self):
        return self.role == 'trainer'

    def is_client(self):
        return self.role == 'client'

    def __str__(self):
        return self.username


class Trainings(models.Model):
    trainer = models.CharField(max_length=100)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_of_training = models.DateTimeField(null=True, blank=True)


    def days_left(self):
        date_of_training = self.date_of_training
        delta = date_of_training - datetime.date.today()
        return max(0, delta.days)

    def get_trainer_username(self):
        trainer = CustomUser.objects.get(id = self.trainer)
        return  trainer.username

    def get_trainer_specialization(self):
        trainer = CustomUser.objects.get(id = self.trainer)
        return trainer.get_specialization_display()