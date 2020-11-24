from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

from django.contrib.auth.models import User
from .models import Customer, Hotel
from .forms import userSignupform, hotelSignupform


# Create your views here.

def login(request):
    context = {}
    if request.method == "POST" and 'loginUser' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            django_login(request, user)
            return redirect('/Userprofile/')
        else:
            context["error"] = "Provide Valid Credentials!!"
            return render(request, 'app/login.html', context)
    
    if request.method == "POST" and 'loginHotel' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            django_login(request, user)
            return redirect('/hotelpage/')
        else:
            context["error"] = "Provide Valid Credentials!!"
            return render(request, 'app/login.html', context)

    else:
        return render(request, 'app/login.html', context)



def hotelSignup(request):
    if request.method == "POST" :
        form = hotelSignupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['BusinessID']
            print(username)
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('/login/')
    else:
        form = hotelSignupform()
    
    return render(request, 'app/hotelSignup.html', {'form': form})


def Userprofile(request):
    user = Customer.objects.get( id = request.user.id )
    args = {'ob': user}
    return render(request, 'app/Userprofile.html', args)

def mainscreen(request):
    return render(request, 'app/mainscreen.html')

def updateUserProfile(request):
    return render(request, 'app/updateUserProfile.html')

def updateHotelProfile(request):
    return render(request, 'app/updateHotelProfile.html')

def hotelpage(request):
    user = Hotel.objects.get(id=1)
    args = {'ob': user}
    return render(request, 'app/hotelpage.html', args)


def userSignup(request):
    if request.method == "POST" :
        form = userSignupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('/login/')
    else:
        form = userSignupform()
    
    return render(request, 'app/userSignup.html', {'form': form})