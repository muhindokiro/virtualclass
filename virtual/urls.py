from django.urls import path
from . import views

urlpatterns = [
    path( '', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('student/', views.studentPage, name="student"),  
	path('lecturer/', views.lecturerPage, name="lecturer"),

]
