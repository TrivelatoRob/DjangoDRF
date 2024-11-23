#school_management_drf/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),  # Incluindo as URLs do app students
    path('api/', include('courses.urls')),  # Incluindo as URLs do app students
    path('api/accounts/', include('accounts.urls'))
]
