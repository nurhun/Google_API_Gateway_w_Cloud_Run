"""moviesapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.schemas import get_schema_view as rest_framework_get_schema_view
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Using trailing_slash=False to bypass trailing slash redirection issue with API.
router = routers.DefaultRouter(trailing_slash=False)

# router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Movies API",
      default_version='v1',
      description="MoviesAPI description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('', lambda request: HttpResponse('Hello World!'), name='hello_world'),

    path('admin/', admin.site.urls),

    # Required for rest_framework_swagger exposed on api/v1/docs
    path('api/v1/api_schema', rest_framework_get_schema_view(
    title='API Schema',
    description='Guide for the REST API'
    ), name='api_schema'),

    path('api/v1/docs', TemplateView.as_view(
    template_name='docs.html',
    extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),

    # /api/v1/movie/
    path('api/v1/', include('movies.urls')),

    # # Allow login for django users apart from /admin/ panel.
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # # gives us access to token auth
    # # curl -XPOST -F 'username=**your_username**' -F 'password=**your_password**' http://localhost:8000/api/v1/api-token-auth/
    # path('api/v1/api-token-auth/', obtain_auth_token),

    path('api/v1/users', include('users.urls')),

    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('ht/', include('health_check.urls')),

    # Used "drf-yasg - Yet another Swagger generator" to get openAPI spec 2.0
    # A JSON view of your API specification at /swagger.json
    # A YAML view of your API specification at /swagger.yaml
    # A swagger-ui view of your API specification at /swagger/
    # A ReDoc view of your API specification at /redoc/
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]