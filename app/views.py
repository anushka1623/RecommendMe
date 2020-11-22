from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import (
     authenticate,
     get_user_model,
     login
)
from .models import Customer
from .forms import userSignupform, loginform

# Create your views here.

def login(request):
    form = loginform(request.POST or None)
    if form.is_valid():
        Username = form.cleaned_data.get('Username')
        password = form.cleaned_data.get('password')
        user = authenticate(Username = Username, password= password)
        login(request, user)
    context ={
        'form':form,
    }
    return render(request, 'app/login.html', context)

def hotelSignup(request):
    return render(request, 'app/hotelSignup.html')

def userSignup(request):
    form = userSignupform(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(Username = user.Username, password= password)
        login(request, new_user)
    context ={
        'form':form,
    }
    return render(request, 'app/userSignup.html', context)


       
