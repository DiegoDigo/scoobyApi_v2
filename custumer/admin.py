from django.contrib import admin
from custumer.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'timestamp', 'active']
    search_fields = ['email']
    list_filter = ['active']
    autocomplete_lookup_fields = {
        'email': ['email'],
        }


admin.site.register(User, AdminUser)

