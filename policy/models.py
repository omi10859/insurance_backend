from statistics import mode
from django.db import models


class UserPolicy(models.Model):

    policy_id = models.IntegerField()
    date_of_purchase = models.DateField()
    customer_id = models.IntegerField()
    fuel = models.CharField(max_length=10)
    vehicle_segment = models.CharField(max_length=2)
    premium = models.IntegerField()
    bodily_injury_liability = models.BooleanField()
    personal_injury_protection = models.BooleanField()
    property_damage_liability = models.BooleanField()
    collision = models.BooleanField()
    comprehensive = models.BooleanField()
    customer_gender = models.CharField(max_length=7)
    customer_income_group = models.CharField(max_length=50)
    customer_region = models.CharField(max_length=20)
    customer_marital_status = models.BooleanField()
