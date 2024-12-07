from django.contrib import admin
from .models import Grade

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'teacher', 'grade', 'date_assigned')  # Exibe as colunas na lista
    list_filter = ('course', 'teacher')  # Permite filtrar por curso e professor
    search_fields = ('student__name', 'course__name', 'teacher__name')  # Permite busca por nome de aluno, curso ou professor
    ordering = ('-date_assigned',)  # Ordena as notas pela data de atribuição, em ordem decrescente

admin.site.register(Grade, GradeAdmin)
