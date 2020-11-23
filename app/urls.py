from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('userSignup/', views.userSignup),
    path('hotelSignup/', views.hotelSignup),
    path('Userprofile/', views.Userprofile),
    path('mainscreen/', views.mainscreen),
    path('updateUserProfile/', views.updateUserProfile),
    path('hotelpage/', views.hotelpage),
    path('updateHotelProfile/', views.updateUserProfile),
    
]