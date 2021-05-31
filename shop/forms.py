from django.db import models
from django.contrib.auth.models import User
from django import forms
from . models import Vendorx ,Customer


class VendorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class vendorx(forms.ModelForm):
    class Meta:
        model= Vendorx
        fields = [ 'ShopNmae','mobile','gender','cnic','age', 'image']
