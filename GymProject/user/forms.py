# forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'phone_number', 'address', 'height', 'weight', 'membership']
        widgets = {
            'membership': forms.Select(choices=Profile.MEMBERSHIP_CHOICES),
        }
