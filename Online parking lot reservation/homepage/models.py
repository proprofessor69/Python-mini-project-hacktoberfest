from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vehicle(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=10)
    registration = models.CharField(max_length=20,primary_key=True,null=False)
    vechicle_manu = models.TextField(max_length=150,default='None')
    vehicle_model = models.TextField(max_length=150, default='None')
    
    
    def __str__(self):
        return self.registration