from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]  # Apenas usuários autenticados podem acessar as views