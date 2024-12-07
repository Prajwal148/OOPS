
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from classes.forms import classform
from .models import GymClass


# Create your views here.
def classes(request):
    # Initialize the form
    form = classform(request.POST or None)

    # Query all classes from the database
    all_classes = GymClass.objects.all()

    # If the form is valid, save it and redirect
    if form.is_valid():
        form.save()
        return redirect('classes')

    # Render the template with both the form and the list of classes
    return render(request, 'classes/classes.html', {'form': form, 'all_classes': all_classes})

def bookings(request):
    template = loader.get_template('classes/bookings.html')
    context = {}
    return HttpResponse(template.render(context, request))

