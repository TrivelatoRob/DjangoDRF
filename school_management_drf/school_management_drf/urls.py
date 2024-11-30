#school_management_drf/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),  # Incluindo as URLs do app students
    path('api/', include('courses.urls')),  # Incluindo as URLs do app students
    path('api/accounts/', include('accounts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
