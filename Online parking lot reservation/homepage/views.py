from pyexpat.errors import messages
from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from homepage.models import Vehicle
from django.contrib.auth.models import User

from project.settings import TEMPLATES

#@login_required(login_url='ac:login')
def home(request):
    return render(request,'homepage/home.html')

@login_required(login_url='ac:login')
def vehicle(request):
    message = ''
    if request.method == 'POST':
        type = request.POST.get('type')
        Registration_number  = request.POST.get('Registration_number')
        vehicle_manu = request.POST.get('vehicle_manu')
        vehicle_model = request.POST.get('vehicle_model')
        try:
            queryset = Vehicle.objects.get(registration = Registration_number )
            message = "Vehicle registration number already exists"
        except:
            form = Vehicle(vehicle_type = type,registration = Registration_number,vechicle_manu = vehicle_manu,vehicle_model = vehicle_model )
            instance = form
            instance.username = request.user
            instance.save()
            return redirect('homepage:show_vehicle')
    return render(request,'homepage/vehicle.html',{'message':message})

@login_required(login_url='ac:login')
def show_vehicle(request):
    form = Vehicle.objects.filter(username = request.user)
    return render(request,'homepage/view_vehicle.html',{'form':form})

@login_required(login_url='ac:login')
def delete_vehicle(request, pk):
    order = Vehicle.objects.get(registration = pk)
    if request.method=='POST':
        order.delete()
        return redirect('/show_vehicle')
    
    context = {'item':order}
    return render(request, 'homepage/delete_vehicle.html',context)

@login_required(login_url='ac:login')
def update_vehicle(request, pk):
    order = Vehicle.objects.get(registration = pk)
    if request.method == 'POST':
        order.delete()
        order.registration = request.POST.get('Registration_number')
        order.vehicle_type = request.POST.get('type')
        order.vechicle_manu = request.POST.get('vehicle_manu')
        order.vehicle_model = request.POST.get('vehicle_model')
        order.save()
        return redirect('/show_vehicle')
    return render(request,'homepage/update_vehicle.html',{'item':order})

def contact_us(request):
    return render(request, 'homepage/contact_us.html')