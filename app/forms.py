from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import Customer, Hotel


class userSignupform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'username',
            'password',
            'FirstName',
            'LastName',
            'Location',
            'foodtype',
            'cuisinetype',
            'DateOfBirth',
            'Email',
            'ContactNo'
        ]

class hotelSignupform(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'HotelName',
            'password',
            'OpeningTime',
            'ClosingTime',
            'TopFoodItems',
            'BusinessID',
            'foodtype',
            'cuisinetype',
            'Location',
            'Email',
            'ContactNo'
        ]


