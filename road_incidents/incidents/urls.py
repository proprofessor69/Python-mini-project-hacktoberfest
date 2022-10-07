from django.urls import path
from . import views

urlpatterns = [
    # Server routes
    path('', views.index, name='index'),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path('log', views.log, name="log"),

    # API routes
    path('add_point', views.add_point, name="add_point"),
    path('send_points', views.send_points, name="send_points"),
    path('remove_point/<int:pointID>', views.remove_point, name="remove_point"),
]