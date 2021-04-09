from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Types de Compte',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'type',
                ),
            },
        ),
    )

class ClientMoreAdminForm(admin.ModelAdmin):
    form = ClientMoreForm



admin.site.register(User, CustomUserAdmin)
admin.site.register(ClientMore, ClientMoreAdminForm)