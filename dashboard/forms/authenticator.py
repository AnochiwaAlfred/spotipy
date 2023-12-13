from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserAuth(AuthenticationForm):
    
    def __init__(self, request, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})
    # def confirm_login_allowed(self, user: AbstractBaseUser) -> None:
    #     return super().confirm_login_allowed(user)