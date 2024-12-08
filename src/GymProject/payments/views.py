from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
import logging
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking
from django.contrib.auth.models import User


# Set up logging (optional)
logger = logging.getLogger(__name__)

def payments(request):
    if request.method == 'POST':
        price = request.POST.get('price', "Not provided")  # Retrieve price from the form
        class_name = request.POST.get('class_name', "Not provided")
        instructor = request.POST.get('instructor', "Not provided")
        start_time = request.POST.get('start_time', "Not provided")
        end_time = request.POST.get('end_time', "Not provided")
        print("Request Data:", request.POST)
        print(f"{price},{class_name},{instructor},{start_time},{end_time}")  # Debug print statement
    else:
        price = "Not provided"

    context = {'price': price,'class_name': class_name,'instructor': instructor,'start_time': start_time,'end_time': end_time,}
    return render(request, 'payments/payments.html', context)


def bookings_Confirmation(request):
    if request.method == 'POST':
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return HttpResponse("You need to be logged in to make a booking.", status=403)

        # Retrieve data from the POST request
        price = request.POST.get('price', "Not provided")
        class_name = request.POST.get('class_name', "Not provided")
        instructor = request.POST.get('instructor', "Not provided")
        start_time = request.POST.get('start_time', "Not provided")
        end_time = request.POST.get('end_time', "Not provided")

        print("Request Data:", request.POST)
        print(f"{price},{class_name},{instructor},{start_time},{end_time}")  # Debug print statement

        # Use the authenticated user (request.user)
        user = request.user

        # Create the booking record
        booking = Booking(
            user=user,
            class_name=class_name,
            instructor=instructor,
            price=price,

        )
        booking.save()

        # Optionally, send a confirmation email or notification

        # Redirect to a confirmation page or render a confirmation template
        context = {
            'price': price,
            'class_name': class_name,
            'instructor': instructor,
            'start_time': start_time,
            'end_time': end_time,
        }
        return render(request, 'Booking_confirmation.html', context)

    else:
        # Handle the case where the request method is not POST
        return HttpResponse("Invalid request method.", status=405)


def user_bookings(request):
    # Fetch bookings for the logged-in user
    bookings = Booking.objects.filter(user=request.user)

    # Pass the bookings to the template
    return render(request, 'user_bookings.html', {'bookings': bookings})
