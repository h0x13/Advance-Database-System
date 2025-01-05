from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User_Account

# Create your views here.

# responsible for users
def landing_page(request):
    return render(request, 'landing-page.html')

# def register(request):
#     return render(request, 'temp_account/register.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User_Account.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'temp_users/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'temp_users/login.html')


# @login_required
def homepage(request):
    return render(request, 'temp_users/homepage.html')

def coffee(request):
    return render(request, 'temp_users/coffee.html')

def profile(request):
    return render(request, 'temp_users/profile.html') 





