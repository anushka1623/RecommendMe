from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('userSignup/', views.userSignup),
    path('hotelSignup/', views.hotelSignup),

    
]