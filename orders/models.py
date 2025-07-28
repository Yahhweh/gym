from django.db import models
from django.utils import timezone
from  people.models import CustomUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from listofgyms.constants import STATUS_CHOICES

class Order(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    first_name = models.CharField(max_length= 200, )
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def update_total(self):
        self.total_price = sum(item.get_total_price() for item in self.items.all())
        self.save()

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def get_total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product} x {self.quantity}"
