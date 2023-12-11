from django.shortcuts import render
# from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
# from rest_framework.decorators import permission_classes


# @permission_classes([IsAdminUser])
# class CustomUserViewSet(UserViewSet):
#     # Your custom view set logic goes here
#     pass