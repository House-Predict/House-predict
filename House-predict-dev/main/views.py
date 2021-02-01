from django.shortcuts import render, redirect
from .forms import add_prop_form,feedbackform
from django.utils import timezone

from .models import Property
import pandas as pd

def main(response):
    return render(response,'main/home.html',{})

def add_property(request):
    if request.method=="POST":
        form=add_prop_form(request.POST)
        if form.is_valid():
            p=form.save()
            request.user.property.add(p)
            return redirect('/profile')
    else:
        form=add_prop_form()
    return render(request,'main/addprop.html',{'form':form})

def show(request,x):
    return render(request,'main/show.html',{'p':Property.objects.get(id=x)})

def about_us(response):
    return render(response,'main/aboutus.html',{})

def contact_us(request):
    if request.method=='POST':
        form=feedbackform(request.POST)
        if form.is_valid():
            x=str(timezone.now())[:10]
            c=form.save(commit=False)
            c.date=x
            c.save()
            return redirect('/home')
        else:
            print(form.errors)
    else:
        form=feedbackform()
    return render(request,'main/contactus.html',{'form':form})

def ml_algo(response):
    return render(response,'main/mlalgo.html',{})

def profile(response):
    return render(response,'main/profile.html',{})

def future(response):
    return render(response,'main/future.html',{})