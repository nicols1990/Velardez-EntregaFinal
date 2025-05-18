from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    username=forms.CharField(label="usuario")
    email=forms.EmailField()
    password1=forms.CharField(label="contrasenia", widget=forms.PasswordInput)          
    password2=forms.CharField(label="Repetir contrasenia", widget=forms.PasswordInput)
    
    
    class Meta:
        model=User
        fields=["username","email","password1", "password2"]
        helps_text={llave:"" for llave in fields}

    