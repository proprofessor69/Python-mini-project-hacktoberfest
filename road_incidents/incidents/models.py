from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Point(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=18)
    longitude = models.DecimalField(max_digits=20, decimal_places=18)
    value = models.CharField(max_length=50)
    openDate = models.DateField(auto_now=False, auto_now_add=True)
    closeDate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} | {self.value}"

    def serialize(self):
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "value": self.value,
            "openDate": self.openDate,
            "closeDate": self.closeDate,
            "user": str(self.user),
            "active": self.active
        }