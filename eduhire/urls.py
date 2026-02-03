"""
Global URL routing for eduhire project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/lms/', include('apps.lms.urls')),
    path('api/coding/', include('apps.coding.urls')),
    path('api/assessments/', include('apps.assessments.urls')),
    path('api/sincerity/', include('apps.sincerity.urls')),
    path('api/finance/', include('apps.finance.urls')),
    path('api/documents/', include('apps.documents.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
