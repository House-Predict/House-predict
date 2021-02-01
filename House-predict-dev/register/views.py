from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import register_form,login_form

def register(request):
    if request.method=="POST":
        form=register_form(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)    
            return redirect('/')
    else:
        form = register_form()
    return render(request,'register/register.html',{"form":form})

def loginv(request):
    if request.method=="POST":
        form=login_form(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/')    
    else:
        form = login_form()
    return render(request,'registration/login.html',{"form":form})

def logoutv(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')