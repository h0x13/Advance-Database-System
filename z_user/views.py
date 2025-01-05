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
from .forms import User_Register, User_Login

# Create your views here.

# responsible for users
def landing_page(request):
    return render(request, 'landing-page.html')

def register(request):
    if request.method == 'POST':
        form = User_Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = User_Register()
    return render(request, 'temp_users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = User_Login(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = User_Login()
    return render(request, 'temp_users/login.html', {'form': form})


# @login_required
def homepage(request):
    return render(request, 'temp_users/homepage.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def coffee(request):
    return render(request, 'temp_users/coffee.html')

def profile(request):
    user_account = User_Account.objects.get(username=request.user)
    print(user_account)

    context = {
        "username": user_account.username,
        "first_name": user_account.first_name,
        "last_name": user_account.last_name,
        "phone_number": user_account.phone_number,
        "email": user_account.email,
        "location": user_account.location,
        "created_at": user_account.created_at
    }

    return render(request, "temp_users/profile.html", context)






