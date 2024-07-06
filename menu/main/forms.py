from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']  # Campos que deseas mostrar en el formulario