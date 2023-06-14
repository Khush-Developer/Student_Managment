from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from student.models import Addcourse,Addstudent


# api for addcourse
class CourseViewSet(generics.ListAPIView):
    queryset = Addcourse.objects.all()
    serializer_class = CourseSerializer


class CreatecourseViewSet(generics.CreateAPIView):
    queryset = Addcourse.objects.all()
    serializer_class = CourseSerializer

class UpdatecourseViewSet(generics.RetrieveUpdateAPIView):
    queryset = Addcourse.objects.all()
    serializer_class = CourseSerializer

class DeletecourseViewSet(generics.DestroyAPIView):
    queryset = Addcourse.objects.all()
    serializer_class = CourseSerializer

# api for addstudent

class ShowStudentViewSet(generics.ListAPIView):
    queryset =Addstudent.objects.all()
    serializer_class = AddStudentSerializer


class CreatestudentViewSet(generics.CreateAPIView):
    queryset = Addstudent.objects.all()
    serializer_class = AddStudentSerializer

class UpdatestudentiewSet(generics.RetrieveUpdateAPIView):
    queryset = Addstudent.objects.all()
    serializer_class = AddStudentSerializer

class DeletestudentViewSet(generics.DestroyAPIView):
    queryset = Addstudent.objects.all()
    serializer_class = AddStudentSerializer
