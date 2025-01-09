from django.contrib import admin
from .models import Admin_Account, Coffee, Order, AdminLogs

# Register your models here.
# admin.site.register(Admin_Account)

@admin.register(Admin_Account)
class Admin_Account(admin.ModelAdmin):
    list_display = ("username", "password", "last_login")


@admin.register(Coffee)
class Coffee(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ("user", "coffee")

@admin.register(AdminLogs)
class AdminLogs(admin.ModelAdmin):
    list_display = ("admin","action", "log_time")

