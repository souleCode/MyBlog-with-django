

from django import forms
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class LoginFrom(AuthenticationForm):
    username= forms.CharField(label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    password=forms.CharField(label='Password ',widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    
class UserForm(UserCreationForm):
    username= forms.CharField(label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    
    email= forms.CharField(label='Email',widget=forms.EmailInput(attrs={
        'class':'form-control',
    }))
    
    password1=forms.CharField(label='Password ',widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    password2=forms.CharField(label='Confirm your password ',widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    
    class Meta:
        model= User
        fields=['username','email','password1','password2',] 
        
class ProfileForm(forms.ModelForm):
    birthday= forms.DateField(label='birthday',widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    phonenumber= forms.IntegerField(label='phonenumber',widget=forms.TextInput(attrs={
        'class':'form-control',
        'type': 'number',
    })) #on utilse pas integerfield pour les vraie application . 
    class Meta:
           model= Profile  
           fields=('birthday','phonenumber')  