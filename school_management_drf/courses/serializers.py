from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Course
from accounts.models import CustomUser

class CourseSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'teacher_name' ]

   
    def validate_name(self, value):
        """
        Validação personalizada para o campo 'name' (nome do curso).
        """
        if len(value.strip()) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value

    def validate_description(self, value):
        """
        Validação personalizada para o campo 'description' (descrição do curso).
        """
        if len(value.strip()) < 3:
            raise serializers.ValidationError("A descrição deve ter pelo menos 3 caracteres.")
        return value
    
    def get_teacher_name(self, obj):
        """
        Método para retornar o nome do professor (assumindo que o modelo Teacher tem um campo 'name').
        """
        return obj.teacher.first_name if obj.teacher else None
    
    
    
