from django.db import models

# Create your models here.

class Posts(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')
    description=models.CharField(max_length=400,null=True)
    

class Profile(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='profilepics')

class chatBoxed(models.Model):
    username=models.CharField(max_length=150)
    texted=models.TextField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)


class score(models.Model):
    username=models.CharField(max_length=150)
    myscore=models.IntegerField(max_length=10)

