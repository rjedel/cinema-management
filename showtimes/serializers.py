from movielist.models import Movie
from rest_framework import serializers

from .models import Cinema, Screening


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = Cinema
        fields = '__all__'


class ScreeningSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())

    class Meta:
        model = Screening
        fields = '__all__'
