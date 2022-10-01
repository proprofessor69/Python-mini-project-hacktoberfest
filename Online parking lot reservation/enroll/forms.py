from django import forms
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2',]
       
        widgets = {
           'first_name':forms.TextInput(attrs={'class':'firstname'}),
           'last_name':forms.TextInput(attrs={'class':'lastname'}),
           'username':forms.TextInput(attrs={'class':'username'}),
           'email':forms.TextInput(attrs={'class':'email'}),
           'password1':forms.PasswordInput(attrs={'class':'pass1'}),
           'password2':forms.PasswordInput(attrs={'class':'pass2'}),
       }