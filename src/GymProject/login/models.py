from django.db import models

class Membership(models.Model):
    membership_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=[('active', 'Active'), ('expired', 'Expired'), ('pending', 'Pending')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

