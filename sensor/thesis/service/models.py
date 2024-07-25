from django.db import models
class Service(models.Model):
    box_number = models.PositiveIntegerField()
    medicine_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()


class Reminder(models.Model):
    medicine_name = models.CharField(max_length=100)
    time_to_take_medicine = models.CharField(max_length=20)  
# Create your models here.
