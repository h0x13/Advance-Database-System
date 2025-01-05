from django import forms

class Admin_Login(forms.Form):
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
