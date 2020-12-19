from movielist.models import Movie
from rest_framework import serializers

from .models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', queryset=Movie.objects.all())

    class Meta:
        model = Cinema
        fields = ("id", "name", "city", "movies")
