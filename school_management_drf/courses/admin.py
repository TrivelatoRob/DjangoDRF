from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'teacher')
    search_fields = ('name', 'description', 'teacher')

# Register your models here.
