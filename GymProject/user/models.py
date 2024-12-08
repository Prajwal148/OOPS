# models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    MEMBERSHIP_CHOICES = [
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # In meters, for example
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # In kg
    membership = models.CharField(
        max_length=10,
        choices=MEMBERSHIP_CHOICES,
        default='silver'
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
