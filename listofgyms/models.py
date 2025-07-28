from django.db import models
from listofgyms.constants import LOCATIONS, MAX_PRICE, MIN_PRICE, MAX_RADIUS, CENTER_LONG, CENTER_LAT
from geopy.distance import lonlat, distance
from people.models import CustomUser
from django.utils import timezone
from datetime import timedelta
from datetime import date
import  datetime


class Gym(models.Model):
    LOCATION_CHOICES = []
    for i in LOCATIONS:
        LOCATION_CHOICES.append((i[0], i[1]))



    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, blank=True)
    description = models.TextField()
    location = models.IntegerField(choices=LOCATION_CHOICES,blank=True,null=True)
    latitude = models.FloatField(max_length=50, auto_created=True)
    longitude = models.FloatField(max_length=50, auto_created=True)
    working_time = models.ForeignKey('WorkingTime',
                                     on_delete=models.CASCADE,
                                     related_name='gym_working_time')
    condition = models.BooleanField(default=False)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        for location_tuple in LOCATIONS:
            loc_id = location_tuple[0]
            name = location_tuple[1]
            if loc_id == self.location:
                self.title = f'GYM {self.id} in {name}'
                self.description = f'good gym in {name}'
                break

        self.latitude = LOCATIONS[self.location][2]
        self.longitude = LOCATIONS[self.location][3]

        gym_distance = distance(lonlat(self.longitude, self.latitude), lonlat(CENTER_LONG, CENTER_LAT)).kilometers
        max_price = 3000
        min_price = 500
        max_radius = 10

        if gym_distance > max_radius:
            self.price =  min_price
        else:

            distance_ratio = gym_distance / MAX_RADIUS
            price_difference = MAX_PRICE - MIN_PRICE

            price = max_price - (distance_ratio * price_difference)
            self.price = int(price)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class WorkingTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.start_time.strftime("%H:%M")} to {self.end_time.strftime("%H:%M")}'


class Subscription(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def calculate_duration(self, start_date, quantity):
            self.end_date = start_date + (quantity * timedelta(days=30))


    def days_left(self):
        end_date = self.end_date.date()
        delta = end_date - date.today()
        return max(0, delta.days)
