from django import forms
from .models import GymClass
from . import models

class classform(forms.ModelForm):
    class Meta:
        model = GymClass
        fields = ('class_name','instructor','start_time','end_time')


