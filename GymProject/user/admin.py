from django.contrib import admin
from login.models import Membership
from .models import Profile

# Register your models here.
admin.site.register(Membership)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone_number', 'address', 'height', 'weight', 'membership')
    search_fields = ('user__username', 'full_name', 'membership')
    list_filter = ('membership',)

admin.site.register(Profile, ProfileAdmin)