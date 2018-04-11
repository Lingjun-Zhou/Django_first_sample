from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


#python manage.py makemigrations
#python manage.py migrate