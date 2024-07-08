from rest_framework import generics
from.models import Author, Book
from.serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response
from .pagination import AuthorPagination,BookPagination
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class=AuthorPagination
    
    

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if 'books' in request.query_params:
            books_serializer = BookSerializer(instance.book_set.all(), many=True)
            data = serializer.data
            data['books'] = books_serializer.data
            return Response(data)
        else:
            return Response(serializer.data)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class=BookPagination

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer