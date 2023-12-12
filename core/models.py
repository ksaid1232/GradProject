from django.db import models

# Create your models here.
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CUSTOMER = 2000
    ROLE_Instructor = 2001
    ROLE_Admin = 2002
    ROLE_CHOICES=[
        (ROLE_CUSTOMER,"Customer"),
        (ROLE_Instructor,"Instructor"),
        (ROLE_Admin,"Admin"),
    ]
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)