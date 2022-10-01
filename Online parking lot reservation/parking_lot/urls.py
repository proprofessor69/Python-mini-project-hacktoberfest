from django.contrib import admin
from django.urls import path
from . import views


app_name = "parking_lot"


urlpatterns = [
   path('parking_lots',views.parking_lots, name="parking_lots"),
   path('show_parking',views.show_parking, name="show_parking"),
   path('delete_parking_lots/<int:pk>',views.delete_parkinglots, name="delete_parking_lots"),
   path('parking_space/<str:pk>',views.parking_space, name="parking_space"),
   path('view_parkingspace/<str:pk>',views.view_parkingspace, name="view_parkingspace"),
   path('book_parking/<int:pk>',views.book_parking, name="book_parking"),
   path('ack/<int:pk>',views.acknowledge,name='acknowledge'),
   path('view_booking',views.view_booking,name='view_booking'),
   path('cancelBookin/<int:pk>',views.cancelBookin,name = "cancelBookin"),
   path('deleteBooking/<int:pk>',views.deleteBooking,name = "deleteBooking"),
   path('view_log/<int:pk>', views.view_log,name= "view_log"),
   path('log/<int:pk>/<str:date>', views.log,name= "log"),
   path('fullslot/<int:id>/<str:date>', views.fullslot,name= "fullslot"),
   path('invalid_time/<int:id>', views.invalid_time,name= "invalid_time"),
   path('your_cancellations',views.your_cancellations,name = "your_cancellations"),
   path('admin_view_cancellation',views.admin_view_cancellation,name = "admin_view_cancellation"),
   path('serach_admin',views.serach_admin,name = "serach_admin"),
]
