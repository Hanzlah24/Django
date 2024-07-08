from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Book, Author
from django.db.models import Q
from .serializers import BookSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from APIs.settings import MESSAGE_RESPONSE

@api_view(['GET'])
def displayRoutes(request):
    routes = ['/books', 'books/:name']
    return Response(routes)




@api_view(['GET', 'POST'])
def books_list(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        books = Book.objects.filter(Q(name__icontains=q) | Q(author__name__icontains=q))
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        author_name = request.data.get('author_name', 'ABC')
        book_name = request.data.get('name', 'XYZ')
        description = request.data.get('description', '')
        
        author, created = Author.objects.get_or_create(name=author_name)
        book = Book.objects.create(name=book_name, description=description, author=author)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)
    
    
class BookDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    def get_object(self,name):
        try:
            return Book.objects.get(name=name)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self,request,name):
        book = self.get_object(name)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)
    def put(self,request,name):
        book = self.get_object(name)
        book.name = request.data.get('name', book.name)
        book.description = request.data.get('description', book.description)
        
        author_name = request.data.get('author_name', '')
        if author_name:
            author, _ = Author.objects.get_or_create(name=author_name)
            book.author = author
        
        book.save()
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)
    
    def delete(self,request,name):
        book = self.get_object(name)
        book.delete()
        return Response(MESSAGE_RESPONSE,status=200)

