from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

from django.contrib.auth.models import User
from .models import Customer
from .forms import userSignupform, loginform


# Create your views here.

def login(request):
    if request.method == "POST":
        form = loginform(request.POST)
        user = authenticate(username=form.data.get('Username'), password=form.data.get('password'))
        django_login(request, user)

    else:
        form = loginform()

    return render(request, 'app/login.html', {'form': form})


def hotelSignup(request):
    return render(request, 'app/hotelSignup.html')

def Userprofile(request):
    return render(request, 'app/Userprofile.html')


def userSignup(request):
    if request.method == "POST":
        form = userSignupform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/login.html')
    else:
        form = userSignupform()
    
    return render(request, 'app/userSignup.html', {'form': form})