from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BaseUser

@admin.register(BaseUser)
class BaseUserAdmin(UserAdmin):
    pass
