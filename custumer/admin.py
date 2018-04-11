from django.contrib import admin
from django.contrib.auth.models import Group
from custumer.models import User, Pet, Profile
from custumer.forms import UserChangeForm


class AdminProfile(admin.ModelAdmin):
    list_display = ['fullname', 'phone']
    search_fields = ['fullname']


class AdminPet(admin.ModelAdmin):
    list_display = ['animal']
    list_filter = ['animal']
    search_fields = ['animal']


class AdminUser(admin.ModelAdmin):
    form = UserChangeForm
    list_display = ['email', 'timestamp', 'active']
    search_fields = ['email']
    list_filter = ['active']
    autocomplete_lookup_fields = {
        'email': ['email'],
    }


admin.site.unregister(Group)
admin.site.register(Profile, AdminProfile)
admin.site.register(Pet, AdminPet)
admin.site.register(User, AdminUser)
