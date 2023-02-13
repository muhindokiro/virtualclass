from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("camera/", views.cameraView, name="camera"),
    path("register/", views.registerPage, name="register"),
    path("profile/", views.userProfile, name="profile"),
    path("login/", views.loginPage, name="login"),
    path("notifications/", views.userNotification, name="notify"),
    path("logout/", views.logoutUser, name="logout"),
    path("student/", views.studentPage, name="student"),
    path("lecturer/", views.lecturerPage, name="lecturer"),
    path("lecturer/upload/", views.upload_file, name="upload_file"),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
