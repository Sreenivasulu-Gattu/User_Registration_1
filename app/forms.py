from django import forms

from app.models import *

class User(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','email','password']
        help_texts = {'username':''}
        

class Profile(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['address','profile_pic']