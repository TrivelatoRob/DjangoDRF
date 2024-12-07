from rest_framework import viewsets
from .models import Grade
from .serializers import GradeSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def perform_create(self, serializer):
        # Adiciona o professor automaticamente ao criar a nota
        serializer.save(teacher=self.request.user)
