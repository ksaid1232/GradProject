from django.urls import path , include
from .views import UserViewSet , TokenObtainPairView
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'', UserViewSet)
router.register(r'wtf', TokenObtainPairView,basename='')
urlpatterns = [
    path("",include(router.urls)),
]