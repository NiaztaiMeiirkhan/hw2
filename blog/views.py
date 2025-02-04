from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article

@api_view(['GET'])
def get_articles(request):
    articles = Article.objects.all()
    data = [{"id": article.id, "title": article.title, "text": article.text, "author": article.author} for article in articles]
    return Response(data)

@api_view(['GET'])
def get_article(request, id):
    try:
        article = Article.objects.get(id=id)
        data = {"id": article.id, "title": article.title, "text": article.text, "author": article.author}
        return Response(data)
    except Article.DoesNotExist:
        return Response({"error": "Article not found"}, status=404)
