from django.contrib import admin
from .models import Admin_Account

# Register your models here.
# admin.site.register(Admin_Account)

@admin.register(Admin_Account)
class Admin_Account(admin.ModelAdmin):
    list_display = ("username", "password", "last_login")
    # search_fields = ("student_id", "first_name", "last_name", "email")
    # readonly_fields = ("student_id",)
