from django.contrib import admin
from .models import User_Account, Purchase_Record

# Register your models here.
@admin.register(User_Account)
class User_Account(admin.ModelAdmin):
    list_display = ("username", "email", "password", "created_at")

@admin.register(Purchase_Record)
class Purchase_Record(admin.ModelAdmin):
    list_display = ("user_account", "order", "purchase_date")

