from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics/')
    school = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profession = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f' {self.user.username} Profile'
    
class File(models.Model):
    fullname = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='files/pdfs/')

 
    
    def __str__(self):
        return self.title
    
