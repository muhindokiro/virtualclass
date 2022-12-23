from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import File

Account = get_user_model()

# from uploads.core.models import Document
class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ["username", "email", "password1", "password2"]

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('fullname', 'title', 'pdf')


