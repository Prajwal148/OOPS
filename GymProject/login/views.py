from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'login/signup.html',{'form':form})

