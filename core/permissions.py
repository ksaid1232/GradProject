from rest_framework.permissions import BasePermission
import models
class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.role and models.User.ROLE_Instructor)
