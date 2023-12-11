from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from .models import Course
from .serializers import CourseListSerializer
from rest_framework.permissions import IsAuthenticated ,IsAdminUser ,AllowAny


@api_view()
@permission_classes([AllowAny])

def courses_list(request):
    # permission_classes=[IsAuthenticated,]
    coureses = Course.objects.all()
    serializer = CourseListSerializer(coureses,many=True)
    return Response(serializer.data)


@api_view()
def courses_detail(request,id):
    return Response(id)