from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all().values()
    return Response(list(books))

@api_view(['GET'])
def get_book(request, id):
    try:
        book = Book.objects.get(pk=id)
        return Response({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'description': book.description,
            'publication_year': book.publication_year,
        })
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)
