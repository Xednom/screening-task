from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_registration.forms import RegistrationForm

from .models import User


class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name")


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name")


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
