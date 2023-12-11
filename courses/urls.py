from django.urls import path
from . import views
from django_api_admin.sites import site

urlpatterns=[
    path('api_admin/', site.urls),
    path("",views.courses_list),
    path("<int:id>/",views.courses_detail),
]