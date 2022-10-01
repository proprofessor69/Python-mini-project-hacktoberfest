from django.contrib import admin
from django.urls import path
from . import views


app_name = "homepage"


urlpatterns = [
   path('',views.home,name="home"),
   path('vehicle',views.vehicle,name = "vehicle"),
   path('show_vehicle',views.show_vehicle,name = "show_vehicle"),
   path('contact_us',views.contact_us,name = "contact_us"),
   path('delete_vehicle/<str:pk>',views.delete_vehicle,name = "delete_vehicle"),
   path('update_vehicle/<str:pk>',views.update_vehicle,name = "update_vehicle"),
]
