from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=35.00  # Setting the default amount to 35 dollars
    )
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('PayPal', 'PayPal'),
            ('Credit Card', 'Credit Card'),
            ('Debit Card', 'Debit Card'),
        ]
    )
    payment_status = models.CharField(
        max_length=50,
        choices=[
            ('completed', 'Completed'),
            ('failed', 'Failed'),
            ('pending', 'Pending'),
        ]
    )
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount}  on {self.payment_date}"


# models.py




class Booking(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)  # Assuming user is logged in and associated with the booking
    class_name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50,
                              default='Confirmed')  # You can add more statuses like 'Pending' or 'Cancelled'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.class_name} booking for {self.user.username}'
