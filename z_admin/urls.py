from django.urls import path
from . import views

# app_name = 'z_admin'

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin-login'), # REDIRECT
    path('admin-logout/', views.admin_logout, name='admin-logout'), # REDIRECT
    path('landing-page/', views.landing_page, name='landing-page'), # READ
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'), # READ
    path('audit-trail/', views.audit_trail, name='audit-trail'), # READ
    path('add-coffee/', views.add_coffee, name='add-coffee'), # CREATE
    path('coffee-view/', views.coffee_view, name='coffee-view'), # READ
    path('edit-coffee/<int:pk>/', views.edit_coffee, name='edit-coffee'), # UPDATE
    path('delete-coffee/<int:pk>/', views.delete_coffee, name='delete-coffee'), # DELETE
]

