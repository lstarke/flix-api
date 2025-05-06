from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):  # obj is Movie
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    # Example without using ORM Avg feature
    # def get_rate(self, obj): # obj is Movie
    #     reviews = obj.reviews.all() # related_name='reviews' in Review model

    #     if reviews:
    #         sum_stars = 0
    #         for review in reviews:
    #             sum_stars += review.stars

    #         return round(sum_stars / reviews.count(), 1)
    #     return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'A data de lançamento não pode ser anterior a 1990'
            )
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'Resumo não deve ter mais que 200 caracteres.'
            )
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)  # 1:N
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):  # obj is Movie
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_review = serializers.IntegerField()
    avg_stars = serializers.FloatField()
