from django.urls import path
from . import views

# app_name = 'z_admin'

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('audit-trail/', views.audit_trail, name='audit-trail'),
]

