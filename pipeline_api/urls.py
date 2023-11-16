"""event URL Configuration

The `urlpatterns` list routes URLs to views.py. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views.py
    1. Add an import:  from my_app import views.py
    2. Add a URL to urlpatterns:  path('', views.py.home, name='home')
Class-based views.py
    1. Add an import:  from other_app.views.py import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from pipeline_api.views import swagger_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ingestion_weather.urls')),
    path('', include('ingestion_bus_delay.urls')),
    path('', include('staging_weather.urls')),
    path('', include('staging_bus_delay.urls')),
    path('', include('enrichment_bus_weather.urls')),
    path('', include('production_star_schema.urls')),

    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            swagger_schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', swagger_schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', swagger_schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
