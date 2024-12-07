from rest_framework import serializers
from .models import Grade
from students.models import Student
from courses.models import Course
from teachers.models import Teacher

class GradeSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()

    class Meta:
        model = Grade
        fields = ['student', 'course', 'teacher', 'grade', 'date_assigned']
