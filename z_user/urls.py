from django.urls import path
from . import views

# app_name = 'z_user'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('coffee/', views.coffee, name='coffee'),
]

