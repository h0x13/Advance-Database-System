from django import forms
from .models import User_Account

class User_Register(forms.Form):
    username = forms.CharField(
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

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    class Meta:
        model = User_Account
        fields = ['username', 'email', 'password', 'confirm_password']

    def save(self, commit=True):
        user = User_Account(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
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