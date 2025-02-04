from django.urls import path
from .views import get_movies, get_movie

urlpatterns = [
    path('movies/', get_movies),
    path('movies/<int:id>/', get_movie),
]
