from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Admin_Login
from .models import Admin_Account


# Create your views here.
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


@login_required(login_url='z_admin:admin-login')
def admin_dashboard(request):
    return render(request, 'temp_admin/admin-dashboard.html')

# @login_required
# def admin_logout(request):
#     logout(request)
#     return redirect('admin_login')


@login_required
def audit_trail(request):
    audit_logs = Admin_Account.objects.all().order_by('-timestamp')
    audit_logs = {"audit_logs": audit_logs}
    return render(request, 'temp_admin/audit-trail.html', audit_logs)