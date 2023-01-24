from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        read_only_fields = (
            "id",
            "created",
            "modified",
        )
        fields = "__all__"
