from genres.models import Genre
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



