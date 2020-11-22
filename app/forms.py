from django import forms
from django.contrib.auth import (
     authenticate,
     get_user_model
)

User = get_user_model()

class userSignupform(forms.ModelForm):
    Username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'Username',
            'password'
        ]
    


    
class loginform(forms.Form):
    Username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        Username = self.cleaned_data.get('Username')
        password = self.cleaned_data.get('password')
    
        if Username and password:
            user = authenticate(Username = Username, password= password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(loginform, self).clean(*args, **kwargs)

