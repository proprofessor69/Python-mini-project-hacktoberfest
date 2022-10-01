from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def login_page(request):
    if request.method == "POST":
       username =  request.POST.get('uname')
       password = request.POST.get('pas')

       user = authenticate(request, username=username , password=password)

       if user is not None:
            login(request, user)
            return redirect('homepage:home')
       else:
           messages.info(request, "Username or password Incorrect")
           return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('homepage:home')

def signup_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was create for ' + user)
            return redirect('/ac/login')
        else:
            messages.error(request,"Password pattern weak or Username already exist")
    form = CreateUserForm()
    return render(request,'signup.html',{'form':form})
