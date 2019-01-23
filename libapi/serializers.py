from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from libapi.models import Book, PublicationHouse

class BookSerializer(ModelSerializer):
  class Meta:
    model = Book
    fields = ('id','title','price','pages', 'published')

class PublicationHouseSerializer(ModelSerializer):
  # book_set = BookSerializer(many=True)
  book_set = PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = PublicationHouse
    fields = ('id','ratings','name', 'book_set')