from rest_framework import generics

from .models import Cinema, Screening
from .serializers import CinemaSerializer, ScreeningSerializer


class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ScreeningListView(generics.ListCreateAPIView):
    serializer_class = ScreeningSerializer

    def get_queryset(self):
        queryset = Screening.objects.all()
        cinema_city = self.request.query_params.get('cinema__city')
        if cinema_city is not None:
            queryset = queryset.filter(cinema__city__icontains=cinema_city)
        return queryset


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
