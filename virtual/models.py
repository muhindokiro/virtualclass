from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    
# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", "Admin"
#         STUDENT = "STUDENT", "Student"
#         LECTURER = "LECTURER", "Lecturer"
        
#     base_role = Role.ADMIN
        
#     role = models.CharField(max_length=50, choices= Role.choices)
        
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args, **kwargs)

# class StudentManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.STUDENT)
    
# class Student(User):

#     base_role = User.Role.STUDENT

#     student = StudentManager()

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "Only for students"
    
# @receiver(post_save, sender=Student)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "STUDENT":
#         StudentProfile.objects.create(user=instance)


# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     student_id = models.IntegerField(null=True, blank=True)
    
# class LecturerManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.LECTURER)


# class Lecturer(User):

#     base_role = User.Role.LECTURER

#     lecturer = LecturerManager()

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "Only for Lecturers"


# class LecturerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     teacher_id = models.IntegerField(null=True, blank=True)


# @receiver(post_save, sender=Lecturer)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "LECTURER":
#         LecturerProfile.objects.create(user=instance)