from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'temp_admin/admin-login.html')


@login_required
def admin_dashboard(request):
    return render(request, 'temp_admin/admin-dashboard.html')

# @login_required
# def admin_logout(request):
#     logout(request)
#     return redirect('admin_login')


def audit_trail(request):
    return render(request, 'temp_admin/audit-trails.html')