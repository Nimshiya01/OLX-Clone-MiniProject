from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . models import Profile, Posts



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude= ['user']
        fields='__all__'

class Reguser(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']
        