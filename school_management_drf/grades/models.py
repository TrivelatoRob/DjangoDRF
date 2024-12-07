from django.db import models
from students.models import Student
from courses.models import Course
from teachers.models import Teacher

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='grades')
    grade = models.DecimalField(max_digits=5, decimal_places=2)  # A nota, com até duas casas decimais
    date_assigned = models.DateField(auto_now_add=True)  # Data em que a nota foi atribuída

    class Meta:
        unique_together = ('student', 'course')  # Cada aluno pode ter uma única nota por curso

    def __str__(self):
        return f'{self.student.name} - {self.course.name} - {self.grade}'
