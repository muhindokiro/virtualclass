from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from virtual.functions.functions import handle_uploaded_file  
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import CreateUserForm,LectureForm
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage

# from uploads.core.models import Document
# from uploads.core.forms import DocumentForm




def home(request):
    return render(request, "home.html")

@login_required(login_url='login')
def studentPage(request):
    return render(request, "student.html")

@login_required(login_url='login')
def lecturerPage(request):
    return render(request, "lecturer.html")

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')

		context = {'form':form}
		return render(request, 'register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username or Password is incorrect')
   
		context = {}
		return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

def upload(request):  
    if request.method == 'POST':  
        file = LectureForm(request.POST, request.FILES)  
        if file.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        file = LectureForm()  
        return render(request,"lecturer.html",{'form':file})  
    
# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'core/simple_upload.html')


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })