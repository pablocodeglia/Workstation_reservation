from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

# Create your models here.


    
class Workstations(models.Model):
    code = models.CharField(primary_key = True, max_length = 9)
    sector = models.CharField(max_length = 50, null= False, default = "general")
    monitors = models.IntegerField(default=0)
    seats = models.IntegerField(default=1)
    in_use = models.BooleanField(default = False)
    photo = models.ImageField(upload_to='workstations/', default="workstations/ws_thumb1.png")
    def __str__(self):
        return f'{self.code}'
    
class Reservations(models.Model):
    workstation_id = models.ForeignKey('Workstations',on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    
    RESERVATION_STATUS = (
        ('a','Available'),
        ('u','Unavailable'),
        ('x','Temporarily Blocked'),
    )

    status = models.CharField(max_length=1, choices=RESERVATION_STATUS, blank=True, default='a')

    def __str__(self):
        return f'Reservation #{self.id}'

class History(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workstation_id = models.ForeignKey('Workstations',on_delete=models.DO_NOTHING)
    history_date = models.DateTimeField()


