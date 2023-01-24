from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .serializers import MovieSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):

    """
    A simple ModelViewSet.
    """
    # trailing comma is mandatory
    # Allow ONLY list & get for any user but all other actions require authentication.
    # Same rules will apply on swagger documentation page /docs
    # view-level permission
    # permission_classes = (IsAuthenticated,)
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
