from rest_framework import serializers
from student.models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addcourse
        fields = '__all__'


class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addstudent
        fields = '__all__'