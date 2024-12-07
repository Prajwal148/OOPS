from django.db import models
import login.models as login
from django.contrib.auth.models import User
class GymClass(models.Model):
    class_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=20.00)
    created_at = models.DateTimeField(auto_now_add=True)

