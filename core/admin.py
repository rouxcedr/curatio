from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Types de Compte',
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