from django import forms
from django.contrib.auth import authenticate
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
            'ProfilePic',
            'ContactNo'
        ]


class loginform(forms.Form):
    Username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        Username = self.cleaned_data.get('Username')
        password = self.cleaned_data.get('password')

        if Username and password:
            user = authenticate(username=Username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(loginform, self).clean(*args, **kwargs)
