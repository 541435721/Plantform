from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserInfo(models.Model):
    User = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=20)
    UserType = models.IntegerField()
    UserPhone = models.CharField(max_length=20)
    UserEmail = models.CharField(max_length=20)
    UserRegTime = models.DateTimeField(auto_now_add=True)
    UserLastLoginTime = models.DateTimeField(auto_now=True)
    UserLoginNum = models.IntegerField()


class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=20)
    ProjectDesc = models.CharField(max_length=200)
    ProjectStatus = models.IntegerField()
    ProjectCreator = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    ProjectCreateTime = models.DateTimeField(auto_now_add=True)
    ProjectLastModifyTime = models.DateTimeField(auto_now=True)
