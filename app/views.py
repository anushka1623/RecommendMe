from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as django_login

from django.contrib.auth.models import User
from .models import Customer
from .forms import userSignupform


# Create your views here.

def login(request):
    context = {}
    if request.method == "POST":
        Username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(request, Username=Username, password=password)
        if user:
            login(request, user)
            return render(request, 'app/Userprofile.html', context)
        else:
            context["error"] = "Provide Valid Credentials!!"
            return render(request, 'app/login.html', context)

    else:
        return render(request, 'app/login.html', context)



def hotelSignup(request):
    context ={}
    context['user'] = request.user
    return render(request, 'app/hotelSignup.html', context)

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