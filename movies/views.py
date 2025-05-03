from django.db.models import Count, Avg
from movies.models import Movie
from movies.serializers import MovieSerializer
from reviews.models import Review
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    
    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_review = Review.objects.count()
        avg_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']


        return response.Response(data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_review': total_review,
            'avg_stars': round(avg_stars, 1) if avg_stars else 0,
            }, status=status.HTTP_200_OK)      