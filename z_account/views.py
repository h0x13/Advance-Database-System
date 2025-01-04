from django.shortcuts import render

# Create your views here.

# responsible for users
def landing_page(request):
    return render(request, 'landing-page.html')

def register(request):
    return render(request, 'temp_account/register.html')

def login(request):
    return render(request, 'temp_account/login.html')

def logout(request):
    return render(request, 'logout.html')




