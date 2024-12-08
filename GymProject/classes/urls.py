from . import views
from django.urls import path

urlpatterns = [
    path('class/',views.classes,name='classes'),
    path('bookings/',views.bookings,name='bookings'),
]
