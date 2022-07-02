from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False) 
    password1 = forms.CharField(label='Nueva Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1', 'password2']
        help_texts = {k:"" for k in fields}



class AvatarForm(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['avatar']


class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Messages
        fields = ['receiver','msg',]
        widgets = {'msg': forms.Textarea(attrs={'cols': 80})}  # widget para agrandar el TextField a 80 columnas