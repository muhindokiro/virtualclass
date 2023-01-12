from django.db import models

# class user(models.Model):

#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
    
# class File(models.Model):
#     fullname = models.CharField(max_length=50)
#     title = models.CharField(max_length=50)
#     pdf = models.FileField(upload_to='files/pdfs/')

class Userdb(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)

    class Meta:
        db_table ='dbuser'

class File(models.Model): 
    fullname = models.CharField(max_length=50)  
    title = models.CharField(max_length=50) 
    pdf = models.FileField(upload_to='files/pdfs/')

    class Meta:
        db_table ='dbfile'
   
    
    def __str__(self):
        return self.title
    
