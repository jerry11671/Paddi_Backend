from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
from drf_yasg import openapi
from rest_framework import permissions

from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView


schema_view = get_swagger_view(title='MentalPaddy')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assessment/', include('assessment.urls')),
    # path('api_doc/', schema_view),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('accounts/', include('accounts.urls')),
    path('journal/', include('journal.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)