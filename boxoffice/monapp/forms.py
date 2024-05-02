from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model




class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username","email", "password1", "password2")