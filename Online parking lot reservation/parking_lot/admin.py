from django.contrib import admin
from .models import Parkinglots,Parkingspaces,Book_parking,Cancel_booking
# Register your models here.
admin.site.register(Parkinglots)
admin.site.register(Parkingspaces)
admin.site.register(Book_parking)
admin.site.register(Cancel_booking)