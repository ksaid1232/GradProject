from typing import Any
from django.db import models
# Create your models here.
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser  
from django.contrib.auth.models import  UserManager  as BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, username, email, password, **extra_fields) :
        extra_fields['role'] = User.ROLE_Admin
        return super().create_superuser(username, email, password, **extra_fields)

class User(AbstractUser):
    ROLE_Customer = 2000
    ROLE_Instructor = 2001
    ROLE_Admin = 2002
    ROLE_CHOICES=[
        (ROLE_Customer,"Customer"),
        (ROLE_Instructor,"Instructor"),
        (ROLE_Admin,"Admin"),
    ]
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    objects = UserManager()


