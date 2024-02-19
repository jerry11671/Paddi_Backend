from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_swagger_view(title='MentalPaddy')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_doc/', schema_view),
    path('accounts/', include('accounts.urls')),
    path('assessment/', include('assessment.urls')),
    path('journal/', include('journal.urls')),
]
