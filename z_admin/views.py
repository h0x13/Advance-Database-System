from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import Admin_Login, Add_Coffee, Edit_Coffee

from .models import Admin_Account, Coffee, Order
from z_user.models import User_Account



# Create your views here.
def landing_page(request):
    return render(request, 'landing-page.html')

def admin_login(request):
    if request.method == 'POST':
        form = Admin_Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = Admin_Login()

    context = {"form": form}
    return render(request, "temp_admin/admin-login.html", context)

def admin_logout(request):
    logout(request)
    return redirect('landing-page')

@login_required(login_url='admin-login')
def admin_dashboard(request):
    active_users = User_Account.objects.all()
    total_orders = Order.objects.all()

    context = {
        'active_users_count': active_users.count(),
        'total_orders_count': total_orders.count(),
    }
    return render(request, 'temp_admin/admin-dashboard.html', context)



# This is the CRUD for the coffee
@login_required(login_url='admin-login')
def add_coffee(request):    # CREATE
    if request.method == 'POST':
        form = Add_Coffee(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin-dashboard'))
    else:
        form = Add_Coffee()
    return render(request, 'temp_admin/add-coffee.html', {'form': form})

@login_required(login_url='admin-login')
def coffee_view(request):    # READ
    coffees = Coffee.objects.all()
    context = {
        'coffees': coffees
    }
    return render(request, 'temp_admin/coffee-view.html', context)

@login_required(login_url='admin-login')
def edit_coffee(request, pk):    # UPDATE
    coffee = Coffee.objects.get(id=pk)
    if request.method == 'POST':
        form = Edit_Coffee(request.POST, instance=coffee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('coffee-view'))
    else:
        form = Edit_Coffee(instance=coffee)
    return render(request, 'temp_admin/edit-coffee.html', {'form': form})

@login_required(login_url='admin-login')
def delete_coffee(request, pk):    # DELETE
    coffee = Coffee.objects.get(id=pk)
    coffee.delete()
    return HttpResponseRedirect(reverse('coffee-view'))





@login_required(login_url='admin-login')
def order_records(request):
    order_of_users = Order.objects.all()

    context = {
        "orders": order_of_users,
    }

    return render(request, 'temp_admin/admin-order.html', context)






@login_required(login_url='admin-login')
def audit_trail(request):
    return render(request, 'temp_admin/audit-trails.html')