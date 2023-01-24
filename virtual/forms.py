from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import File,Profile

# from uploads.core.models import Document
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('fullname', 'title', 'pdf')

class UpdateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ["image", "school", "phone", "profession"]
