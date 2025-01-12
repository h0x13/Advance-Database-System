from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import User_Register, User_Login, Edit_Form, Select_Quantity, Comment_Form

from z_admin.models import Coffee, Order
from .models import User_Account, Purchase_Record, Users_Feedback


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
def coffee(request, pk=None):
    coffees = Coffee.objects.all()
    user = User_Account.objects.get(username=request.user)

    COFFEE = None
    users_comment = None

    if pk:  # Fetch the selected coffee and its comments
        COFFEE = get_object_or_404(Coffee, pk=pk)
        users_comment = Users_Feedback.objects.filter(coffee=COFFEE)

    # Load all comments for reviews regardless of pk
    all_comments = Users_Feedback.objects.all()

    if request.method == 'POST':
        form = Select_Quantity(request.POST, instance=user)
        comment_form = Comment_Form(request.POST)

        # Process quantity form
        if form.is_valid() and COFFEE:
            quantity = form.cleaned_data.get('quantity')
            Order.objects.create(user=user, coffee=COFFEE, quantity=quantity)
            Purchase_Record.objects.create(user_account=user, order=COFFEE, quantity=quantity)
            messages.success(request, 'Order placed successfully!')
            return redirect('coffee', pk=pk)

        # Process comment form
        if comment_form.is_valid() and COFFEE:
            comment = comment_form.cleaned_data.get('comment')
            Users_Feedback.objects.create(user=user, coffee=COFFEE, comment=comment)
            messages.success(request, 'Comment submitted successfully!')
            return redirect('coffee', pk=pk)

        # Handle invalid forms
        if not form.is_valid():
            messages.error(request, 'Error placing order. Please try again.')
        if not comment_form.is_valid():
            messages.error(request, 'Error submitting comment. Please try again.')

    else:  # GET request
        form = Select_Quantity(instance=user)
        comment_form = Comment_Form()

    # Prepare context
    context = {
        'form': form,
        'coffees': coffees,
        'comments': comment_form,
        'all_comments': all_comments,  # Load all comments for reviews
        'selected_coffee': COFFEE,  # Pass the selected coffee for reference
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


# This is the edit profile page
@login_required(login_url='login')
def edit_profile(request):
    user_account = User_Account.objects.get(username=request.user)
    if request.method == 'POST':
        form = Edit_Form(request.POST, instance=user_account)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = request.user
            user.username = username
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)

            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = Edit_Form(instance=user_account)
    return render(request, 'temp_users/edit-profile.html', {'form': form})






# @login_required(login_url='login')
# def users_feedback(request):
#     if request.method == 'POST':
#         form = Comment_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('coffee'))
#     else:
#         form = Comment_Form()
#     return render(request, 'temp_users/register.html', {'form': form})

















