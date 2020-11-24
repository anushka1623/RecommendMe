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

def arribamexicangrill(request):
    return render(request, 'app/arribamexicangrill.html')

def casinoarizona(request):
    return render(request, 'app/casinoarizona.html')

def chopandwok(request):
    return render(request, 'app/chopandwok.html')

def defacloitaliangrocery(request):
    return render(request, 'app/defacloitaliangrocery.html')

def flosnewasiancuisine(request):
    return render(request, 'app/flosnewasiancuisine.html')

def flowerchild(request):
    return render(request, 'app/flowerchild.html')

def francositaliancaffe(request):
    return render(request, 'app/francositaliancaffe.html')

def freshmint(request):
    return render(request, 'app/freshmint.html')

def georgesonsasiancuisine(request):
    return render(request, 'app/georgesonsasiancuisine.html')
    
def guidoschicagomeatdeli(request):
    return render(request, 'app/guidoschicagomeatdeli.html')

def habanero(request):
    return render(request, 'app/habanero.html')

def indianparadise(request):
    return render(request, 'app/indianparadise.html')

def jadepalace(request):
    return render(request, 'app/jadepalace.html')

def lasthaicuisine(request):
    return render(request, 'app/lasthaicuisine.html')

def loloschickenwaffles(request):
    return render(request, 'app/loloschickenwaffles.html')

def losolivosmexicanpatio(request):
    return render(request, 'app/losolivosmexicanpatio.html')

def mallesthaibistro(request):
    return render(request, 'app/mallesthaibistro.html')

def mercifrenchcafepatisserie(request):
    return render(request, 'app/mercifrenchcafepatisserie.html')

def pfchangs(request):
    return render(request, 'app/pfchangs.html')

def postinokierland(request):
    return render(request, 'app/postinokierland.html')

def simonshotdogs(request):
    return render(request, 'app/simonshotdogs.html')

def solmexicancocina(request):
    return render(request, 'app/solmexicancocina.html')

def tajmahal(request):
    return render(request, 'app/tajmahal.html')

def takedathai(request):
    return render(request, 'app/takedathai.html')

def tandooritimes(request):
    return render(request, 'app/tandooritimes.html')

def taverngrillescottsdale(request):
    return render(request, 'app/taverngrillescottsdale.html')

def thaihouse(request):
    return render(request, 'app/thaihouse.html')

def tuttisanti(request):
    return render(request, 'app/tuttisanti.html')

def zincbistro(request):
    return render(request, 'app/zincbistro.html')

def mainrated(request):
    return render(request,'app/mainscreenRated.html')
def indian(request):
    return render(request,'app/indian.html')
def china(request):
    return render(request,'app/china.html')
def french(request):
    return render(request,'app/french.html')
def indo(request):
    return render(request,'app/Indo.html')
def italy(request):
    return render(request,'app/Italy.html')
def thai(request):
    return render(request,'app/thai.html')
def greece(request):
    return render(request,'app/greece.html')
def morroco(request):
    return render(request,'app/morroco.html')
def veg(request):
    return render(request,'app/veg.html')
def nveg(request):
    return render(request,'app/nonveg.html')





def updateUserProfile(request):
    return render(request, 'app/updateUserProfile.html')

def updateHotelProfile(request):
    return render(request, 'app/updateHotelProfile.html')

def hotelpage(request):
    user = Hotel.objects.get(id=3)
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