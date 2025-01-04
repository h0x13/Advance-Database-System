from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request, 'temp_admin/admin-login.html')