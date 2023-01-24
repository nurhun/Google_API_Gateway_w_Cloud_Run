from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter(trailing_slash=False)
# router = routers.DefaultRouter()

router.register('', viewset=views.MovieViewSet)

urlpatterns = [
    path('movie', include(router.urls))
]