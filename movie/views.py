from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie

@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    data = [{"id": movie.id, "title": movie.title, "description": movie.description, "producer": movie.producer, "duration": movie.duration} for movie in movies]
    return Response(data)

@api_view(['GET'])
def get_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
        data = {"id": movie.id, "title": movie.title, "description": movie.description, "producer": movie.producer, "duration": movie.duration}
        return Response(data)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)
