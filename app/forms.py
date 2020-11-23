from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import Customer


class userSignupform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'Username',
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
