from django.urls import path
from . import views

urlpatterns = [
    path('', views.payments, name='payments'),
    # urls.py
    path('booking_confirmation/', views.bookings_Confirmation, name='booking_confirmation'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),

    # Other paths...
]
