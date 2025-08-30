from django import forms
from .models import Thought
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['text','photo']



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ('username', 'email' , 'password1','password2')