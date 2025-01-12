from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Q

from django.utils import timezone
from django.db.models import Count
from datetime import timedelta, datetime


from .forms import Admin_Login, Add_Coffee, Edit_Coffee

from .models import Admin_Account, Coffee, Order, AdminLogs
from z_user.models import User_Account, Users_Feedback



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
                admin_account = Admin_Account.objects.get(username=username)
                AdminLogs.objects.create(admin=admin_account, action='login') # save to admin logs [login]
                return redirect('admin-dashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = Admin_Login()

    context = {"form": form}
    return render(request, "temp_admin/admin-login.html", context)

def admin_logout(request):
    if request.user.is_authenticated: 
        username = request.user.username  
        admin_account = Admin_Account.objects.get(username=username)
        AdminLogs.objects.create(admin=admin_account, action='logout')

    logout(request)
    return redirect('landing-page')




@login_required(login_url='admin-login')
def admin_dashboard(request):
    active_users = User_Account.objects.all()
    order_of_users = Order.objects.all()
    user_comments = Users_Feedback.objects.all()


    today = timezone.now().date()
    
    # Get the start of today (midnight)
    start_of_today = timezone.make_aware(datetime.combine(today, datetime.min.time()))
    
    # Get the start of yesterday (midnight)
    yesterday = today - timedelta(days=1)
    start_of_yesterday = timezone.make_aware(datetime.combine(yesterday, datetime.min.time()))

    total_orders_today = Order.objects.filter(order_at__gte=start_of_today).count()
    total_orders_yesterday = Order.objects.filter(order_at__gte=start_of_yesterday, order_at__lt=start_of_today).count()

    # Calculate the percentage change if there were orders yesterday
    if total_orders_yesterday > 0:
        percentage_change = ((total_orders_today - total_orders_yesterday) / total_orders_yesterday) * 100
    else:
        percentage_change = 100  


    total_price = Order.objects.aggregate(total=Sum('coffee__price'))['total'] or 0
    context = {
        'active_users_count': active_users.count(),
        'total_orders_count': order_of_users.count(),

        "percentage_change": round(percentage_change, 2),

        "orders": order_of_users[:7], # Responsible for fetching in order table
        "total": total_price,

        "num_comments": user_comments.count(),
        "user_comments": user_comments[:3],
    }
    return render(request, 'temp_admin/admin-dashboard.html', context)













# This is the CRUD for the coffee
@login_required(login_url='admin-login')
def add_coffee(request):    # CREATE
    if request.method == 'POST':
        form = Add_Coffee(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = request.user.username  
            admin_account = Admin_Account.objects.get(username=username)
            AdminLogs.objects.create(admin=admin_account, action='create')
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
            username = request.user.username  
            admin_account = Admin_Account.objects.get(username=username)
            AdminLogs.objects.create(admin=admin_account, action='update')
            return HttpResponseRedirect(reverse('coffee-view'))
    else:
        form = Edit_Coffee(instance=coffee)
    return render(request, 'temp_admin/edit-coffee.html', {'form': form})

@login_required(login_url='admin-login')
def delete_coffee(request, pk):    # DELETE
    coffee = Coffee.objects.get(id=pk)
    coffee.delete()
    username = request.user.username  
    admin_account = Admin_Account.objects.get(username=username)
    AdminLogs.objects.create(admin=admin_account, action='delete')
    return HttpResponseRedirect(reverse('coffee-view'))





@login_required(login_url='admin-login')
def order_records(request):
    order_of_users = Order.objects.all()
    
    for order in order_of_users:
        product = order.quantity * order.coffee.price
        order.total = product

    context = {
        "orders": order_of_users,
    }

    return render(request, 'temp_admin/admin-order.html', context)






@login_required(login_url='admin-login')
def audit_trail(request):
    search_query = request.GET.get('search', '')  # Search term
    action_filter = request.GET.get('action', '')  # Selected action from the dropdown

    logs = AdminLogs.objects.all()

    if search_query:
        logs = logs.filter(
            Q(admin__username__icontains=search_query) |  # Search by admin username (if Admin_Account has a 'username' field)
            Q(action__icontains=search_query)             # Search by action
        )

    if action_filter and action_filter != 'All Actions':
        logs = logs.filter(action__iexact=action_filter)

    context = {
        "logs": logs,
        "search_query": search_query,
        "action_filter": action_filter,
    }

    return render(request, 'temp_admin/audit-trails.html', context)


@login_required(login_url='user-list')
def user_list(request):
    active_users = User_Account.objects.all()

    context = {
        "users": active_users,
    }

    return render(request, 'temp_admin/user-list.html', context)