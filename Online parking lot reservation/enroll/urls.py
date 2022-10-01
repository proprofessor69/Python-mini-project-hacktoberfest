from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ac'

urlpatterns = [
   path('login',views.login_page,name="login"),
   path('signup',views.signup_page,name="signup"),
   path('logout',views.logoutUser,name="logout"),
]
