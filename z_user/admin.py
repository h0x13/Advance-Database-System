from django.contrib import admin
from .models import User_Account

# Register your models here.
@admin.register(User_Account)
class User_Account(admin.ModelAdmin):
    list_display = ("username", "email", "password", "created_at")

