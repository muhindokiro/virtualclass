from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# from notification.models import Notification
from django.db.models.signals import post_save

class Profile(models.Model):
    NOTIFICATION_TYPES = ((1, 'Save'), (2, 'Unsave'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics/')
    school = models.CharField(max_length=200, null=True)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES, null=True)
    phone = models.CharField(max_length=200, null=True)
    profession = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f' {self.user.username} Profile'
    
class File(models.Model):
    fullname = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='files/pdfs/')
<<<<<<< HEAD

 
=======
    date = models.DateTimeField(auto_now_add=True, null=True)
    save_pdf = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save_pdf', null=True)

    def user_save_pdf(sender, instance, *args, **kwargs):
        save = instance
        save_pdf = save.save_pdf
        sender = save.user

        notify = Profile(sender=sender, user=save_pdf, notification_type=1)
        notify.save()

>>>>>>> db36f435831236035081cc10dbc8e657792a3cd0
    
    def __str__(self):
        return self.title
   
# class Notify(models.Model):
#     save_pdf = models.ForeignKey(User, on_delete=models.CASCADE, related_name='save_pdf', null=True)

#     def user_save_pdf(sender, instance, *args, **kwargs):
#         save = instance
#         save_pdf = save.save_pdf
#         # sender = save.user

#         notify = Profile(sender=sender, user=save_pdf, notification_type=1)
#         notify.save()

#Save
post_save.connect(File.user_save_pdf, sender=File)