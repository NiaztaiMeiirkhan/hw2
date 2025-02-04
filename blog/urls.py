from django.urls import path
from .views import get_articles, get_article

urlpatterns = [
    path('articles/', get_articles),
    path('articles/<int:id>/', get_article),
]
