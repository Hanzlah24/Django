from rest_framework.serializers import ModelSerializer
from .models import Book,Author



class AuthorSerializer(ModelSerializer):
    class Meta:
        model=Author
        fields=['name']
        
        
class BookSerializer(ModelSerializer):
    author=AuthorSerializer()
    class Meta:
        model=Book
        fields=['name','description','author']