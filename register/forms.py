from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class register_form(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'type':"password",'class':"form-control",'id':"pass1",'placeholder':"Enter Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'type':"password",'class':"form-control",'id':"pass2",'placeholder':"Confirm Password"}))
    
    class Meta:
        model=User
        fields=("first_name","last_name","username","email","password1","password2")
        widgets={
            'first_name':forms.TextInput(attrs={'type':"text",'class':"form-control",'id':"fname",'placeholder':"First Name"}),
            'last_name':forms.TextInput(attrs={'type':"text",'class':"form-control",'id':"lname",'placeholder':"Last Name"}),
            'username':forms.TextInput(attrs={'type':"text",'class':"form-control",'id':"uname",'placeholder':"Username"}),
            'email':forms.EmailInput(attrs={'type':"email",'class':"form-control",'id':"email",'placeholder':"Email"}),
        }

class login_form(AuthenticationForm):
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'id':"usname",'placeholder':"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':"password",'class':"form-control",'id':"pass",'placeholder':"Password"}))