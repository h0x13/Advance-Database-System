from django import forms
from .models import Coffee

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


class Add_Coffee(forms.ModelForm):
    # image = forms.ImageField(
    #     widget=forms.FileInput(
    #         attrs={
    #             'class': 'form-control'
    #             }
    #     ),
    #     required=True,
    # )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    class Meta:
        model = Coffee
        fields = ['name', 'price']

    def save(self, commit=True):
        coffee = Coffee(
            name=self.cleaned_data['name'],
            price=self.cleaned_data['price'],
        )
        if commit:
            coffee.save()
        return coffee
    

class Edit_Coffee(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
                }
        ),
        required=True,
    )

    class Meta:
        model = Coffee
        fields = ['name', 'price']