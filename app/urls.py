from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('userSignup/', views.userSignup),
    path('hotelSignup/', views.hotelSignup),
    path('Userprofile/', views.Userprofile),
    
]