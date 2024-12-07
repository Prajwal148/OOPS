from . import views
from django.urls import path

urlpatterns = [
    path('profile/',views.profile_view,name='profile'),
    path('userprofile/',views.userprofile,name='userprofile')
]
