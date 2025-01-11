from django import forms
from .models import User_Account
from z_admin.models import Order
from z_user.models import Users_Feedback

class User_Register(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    class Meta:
        model = User_Account
        fields = ['username', 'first_name','last_name', 'phone_number', 'email', 'password', 'location']

    def save(self, commit=True):
        user = User_Account(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone_number=self.cleaned_data['phone_number'],
            location=self.cleaned_data['location'],
        )
        if commit:
            user.save()
        return user



class User_Login(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )



class Edit_Form(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    class Meta:
        model = User_Account
        fields = ['username', 'first_name','last_name', 'phone_number', 'email', 'password', 'location']


class Select_Quantity(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    class Meta:
        model = Order
        fields = ['quantity']





class Comment_Form(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'name': 'review',
                'rows': 3,
                'placeholder': 'Write your review...'
            }
        ),
        required=True,
    )

    class Meta:
        model = Users_Feedback
        fields = ['comment']