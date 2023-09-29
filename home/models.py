from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length= 122)
    email = models.EmailField(max_length= 122)
    phone = models.IntegerField()
    mess = models.TextField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Users(models.Model):
    name = models.CharField(max_length= 122)
    email = models.EmailField(max_length= 122)
    username = models.CharField(max_length= 122)
    password = models.CharField(max_length=122)

    def __str__(self):
        return self.name