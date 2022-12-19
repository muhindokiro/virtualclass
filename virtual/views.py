from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from virtual.functions.functions import handle_uploaded_file
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from .decorators import allowed_users,admin_only

# Create your views here.
from django.core.files.storage import FileSystemStorage
from .models import File,Customer
from .forms import CreateUserForm,FileForm

from django.conf import settings

def home(request):
    return render(request, "home.html")


@login_required(login_url="login")
@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, "student.html")


@login_required(login_url="login")
@allowed_users(allowed_roles=['lecturer'])
def lecturerPage(request):
    files = File.objects.all()
    return render(request, "lecturer.html", {'files': files})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + username)

                group = Group.objects.get(name='student')
                user.groups.add(group)
                
                return redirect("login")

        context = {"form": form}
        return render(request, "register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or Password is incorrect")

        context = {}
        return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
@allowed_users(allowed_roles=['lecturer'])
def upload_file(request):
    if request.method == 'POST':
        form =  FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lecturer')
    else:
        form = FileForm()
    return render(request, "upload.html", {'form': form})




