from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    Firstname= forms.CharField(max_length=100)
    Lastname= forms.CharField(max_length=100)
    Phone= forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','Firstname','Lastname','Phone','email','password1','password2']