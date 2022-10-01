from statistics import mode
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
from homepage.models import Vehicle
import parking_lot

# Create your models here.
class Parkinglots(models.Model):
    parking_lot_id = models.AutoField(primary_key = True)
    no_of_spaces = models.IntegerField(null= False)
    parking_lot_address = models.TextField(max_length=200,default="")
    parking_lot_zipcode = models.BigIntegerField()
  
    def __str__(self):
        return str(self.parking_lot_id)



class Parkingspaces(models.Model):
    parking_lot_id= models.ForeignKey(Parkinglots,on_delete=CASCADE)

    def __str__(self):
        return str(self.id)

class Book_parking(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    vehicle = models.ForeignKey(Vehicle,null = False,on_delete=CASCADE)
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    parking_space_id = models.ForeignKey(Parkingspaces,on_delete=CASCADE)
    parking_lot_id = models.ForeignKey(Parkinglots,on_delete=CASCADE)
    is_cancled = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Cancel_booking(models.Model):
    cancel_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book_parking,on_delete=models.CASCADE)
    reason = models.TextField(max_length=1000,default="Empty")
    cancellation_date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.cancel_id)
