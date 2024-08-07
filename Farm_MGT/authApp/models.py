from django.db import models

# Create your models here

class Contact(models.Model):
    name: str = models.CharField(max_length=50)
    email: str = models.EmailField(max_length=80)
    subject: str = models.CharField(max_length=50)
    message: str = models.TextField(max_length=200)


