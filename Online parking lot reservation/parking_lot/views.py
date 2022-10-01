from nturl2path import url2pathname
from django.contrib.auth.forms import UsernameField
from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Parkinglots,Book_parking,Cancel_booking
from .models import Parkingspaces
from homepage.models import Vehicle
from enroll.forms import User
from time import time
from django.contrib.auth.decorators import login_required
from datetime import datetime as dt
from django.contrib import messages


def parking_lots(request):
    if request.method == 'POST':
        spaces = request.POST.get('spaces')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        form = Parkinglots(no_of_spaces = spaces,parking_lot_address=address,parking_lot_zipcode = zipcode)
        form.save()
        space = int(spaces)
        for i in range(space):
            item = Parkingspaces(parking_lot_id_id = form.parking_lot_id)
            item.save()
        return redirect('parking_lot:show_parking')
    
    return render(request,'parking_lots/parking_lots.html')

def show_parking(request):
    form = Parkinglots.objects.all()
    return render(request,'parking_lots/show_parking.html',{'form':form})

def delete_parkinglots(request, pk):
    order = Parkinglots.objects.get(parking_lot_id = pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/pl/show_parking')
    return render(request, 'parking_lots/delete_parking.html',{'item':order})

def parking_space(request,pk):
    order = Parkinglots.objects.get(parking_lot_id = pk)
    if request.method == 'POST':
        parking_lot_id = request.POST.get('parking_lot_id')
        form =Parkingspaces(parking_lot_id_id = parking_lot_id)
        form.save()
    return render(request,'parking_lots/parking_space.html',{'item':order})

def view_parkingspace(request,pk):
    order = Parkinglots.objects.get(parking_lot_id = pk)
    item = Parkingspaces.objects.filter(parking_lot_id = order.parking_lot_id)
    char = 'N'
    return render(request,'parking_lots/view_parkingspace.html',{'form':order,'data':item,'char':char})

@login_required(login_url='ac:login')
def book_parking(request,pk):
    order = Parkingspaces.objects.get(id = pk)
    order3 = Parkinglots.objects.get(parking_lot_id = order.parking_lot_id_id)
    order2 = Vehicle.objects.filter(username_id = request.user.id)
    logged = request.user.id
    item = 0
    messages = ''
    if request.method == 'POST':
        user_id = request.user.id
        registration = request.POST.get('vehicle_reg')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        parking_space_id = pk
        parking_lot_id = order3.parking_lot_id
        try:
            form = Book_parking(user_id_id=user_id,vehicle_id = registration, date = date, from_time = start_time, to_time = end_time, parking_space_id_id = parking_space_id ,parking_lot_id_id = parking_lot_id)

            ap = str(start_time)
            apl = str(end_time)
            a=dt.strptime(ap,"%H:%M")
            b=dt.strptime(apl,"%H:%M")
            if a>b:
                return redirect('parking_lot:invalid_time',parking_space_id)
        
            obj = Book_parking.objects.filter(date = date,parking_space_id_id = parking_space_id,is_cancled=0)
            for i in obj:
                ab = str(i.from_time)
                bc = str(i.to_time)
                cd = str(start_time)
                ef = str(end_time)
                a=dt.strptime(ab,"%H:%M:%S")
                b=dt.strptime(bc,"%H:%M:%S")
                c=dt.strptime(cd,"%H:%M")
                d=dt.strptime(ef,"%H:%M")
                if ((c>=a and c<=b) or (d>=a and d<=b)) or ((c<=a and d>=b)):
                    return redirect('parking_lot:fullslot', parking_space_id,date)
            form.save()
            return redirect('parking_lot:acknowledge',form.id)
        except:
            messages = "Please fill all the fields"
    context = {'item':order,'item2':order2,'item4':logged,'query':item,'message':messages}
    return render(request,'parking_lots/book_parking.html',context )

def cancelBookin(request, pk):
    order = Book_parking.objects.get(id = pk)
    context = {'item':order}
    return render(request,'parking_lots/cancelBooking.html',context)

def deleteBooking(request,pk):
    order = Book_parking.objects.get(id = pk)
    if request.method == 'POST':
        reason = request.POST.get('reason')
        order2 = Cancel_booking(book_id_id = order.id,reason = reason)
        order.is_cancled = 1
        order.save()
        order2.save()
    return redirect('parking_lot:view_booking')

def acknowledge(request,pk):
    order = Book_parking.objects.get(id = pk)
    order2 = Parkinglots.objects.get(parking_lot_id = order.parking_lot_id_id)
    order3 = Vehicle.objects.get(registration = order.vehicle_id )
    return render(request,'parking_lots/ack.html',{'form':order,'form2':order2,'form3':order3})

@login_required(login_url='ac:login')
def view_booking(request):
    order = request.user
    order2 = Book_parking.objects.filter(user_id_id = order, is_cancled = 0)
    context = {'item':order,'item2':order2}
    return render(request,'parking_lots/view_booking.html',context)

def view_log(request,pk):
    order = Parkingspaces.objects.get(id = pk)
    if request.method == 'POST':
        date = request.POST.get('date')
        return redirect('parking_lot:log',order.id,date)
    return render(request,'parking_lots/view_log.html',{'item':order})

def log(request,pk,date):
    order = Book_parking.objects.filter(parking_space_id = pk,date =date,is_cancled = 0)
    return render(request,'parking_lots/logs.html',{'item':order,'item2':pk,'item3':date})



def fullslot(request,id,date):
    context = {'item1':date,'item2':id}
    return render(request,'parking_lots/fullslot.html',context)

def invalid_time(request,id):
    return render(request,'parking_lots/invalid_time.html',{'id':id})

@login_required(login_url='ac:login')
def your_cancellations(request):
    order = Cancel_booking.objects.filter(book_id__user_id = request.user)
    context = {'item':order}
    return render(request,'parking_lots/your_cancellations.html',context)

def admin_view_cancellation(request):
    order = Cancel_booking.objects.all()
    context = {'item':order}
    return render(request,'parking_lots/your_cancellations.html',context)

def serach_admin(request):
    if request.method == 'POST':
        try:
            user = request.POST.get('user')
            order = Cancel_booking.objects.filter(book_id__user_id = user)
            context = {'item':order}
            return render(request,'parking_lots/your_cancellations.html',context)
        except:
            return redirect('parking_lot:admin_view_cancellation')