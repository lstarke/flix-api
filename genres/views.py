from genres.models import Genre
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.serializers import GenreSerializer
from genres.permissions import GenrePermission

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



