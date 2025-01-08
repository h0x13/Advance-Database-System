from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import User_Register, User_Login

from z_admin.models import Coffee, Order
from .models import User_Account, Purchase_Record


# Create your views here.

# This is the landing page
def landing_page(request):
    return render(request, 'landing-page.html')


# This is the register page
def register(request):
    if request.method == 'POST':
        form = User_Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = User_Register()
    return render(request, 'temp_users/register.html', {'form': form})

# This is the login page
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

# This is the logout page
def user_logout(request):
    logout(request)
    return redirect('landing-page')



# This is the homepage
@login_required(login_url='login')
def homepage(request):
    return render(request, 'temp_users/homepage.html')


# This is the view coffee page
@login_required(login_url='login')
def coffee(request):
    coffees = Coffee.objects.all()
    context = {
        'coffees': coffees
    }
    return render(request, 'temp_users/coffee.html', context)





# This is the profile page
@login_required(login_url='login')
def profile(request):
    user_account = User_Account.objects.get(username=request.user)
    purchase = Purchase_Record.objects.filter(user_account=user_account)


    context = {
        "username": user_account.username,
        "first_name": user_account.first_name,
        "last_name": user_account.last_name,
        "phone_number": user_account.phone_number,
        "email": user_account.email,
        "location": user_account.location,
        "created_at": user_account.created_at, 

    
        "purchase": purchase, # This is the purchase record
        "purchase_count": purchase.count(),
    }
    return render(request, "temp_users/profile.html", context)



# This is the order coffee page
@login_required(login_url='login')
def order_coffee(request, pk):
    coffee = get_object_or_404(Coffee, id=pk)
    user = User_Account.objects.get(username=request.user)
    Order.objects.create(user=user, coffee=coffee)
    Purchase_Record.objects.create(user_account=user, order=coffee)
    return redirect('coffee')
