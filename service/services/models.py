from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from clients.models import Client
from .tasks import set_price

class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )
    plan_type  = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0, 
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])
    
    def __str__(self):
        if self.discount_percent == 0:
            return f'No discount'
        return f"Discount: {self.discount_percent}%"


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)
    price = models.PositiveIntegerField(default=0)

    def save(self, *args, save_model=True, **kwargs):
        if save_model:
            set_price.delay(self.id)
        return super().save(*args, **kwargs)
    
    # hello