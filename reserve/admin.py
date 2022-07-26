from django.contrib import admin

from .models import  History, Reservations, Workstations

# Register your models here.


admin.site.register(Workstations),
admin.site.register(Reservations),
admin.site.register(History),