from django.shortcuts import render
from djoser.views import UserViewSet as BaseUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView

# Create your views here.
class UserViewSet(BaseUserViewSet):
    pass

