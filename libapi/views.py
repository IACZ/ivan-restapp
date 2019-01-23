from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from libapi.models import Book, PublicationHouse
from libapi.serializers import BookSerializer, PublicationHouseSerializer

# Create your views here.

class BookList(ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

'''class PublicationHouseListCreate(ListCreateAPIView):
  queryset = PublicationHouse.objects.all()
  serializer_class = PublicationHouseSerializer

class PubRetUpdateDelete(RetrieveUpdateDestroyAPIView):
  queryset = PublicationHouse.objects.all()
  serializer_class = PublicationHouseSerializer'''

class PublicationViewSet(ModelViewSet):
  # queryset = PublicationHouse.objects.all()
  serializer_class = PublicationHouseSerializer

  def get_queryset(self):
    ratings = self.request.query_params.get('ratings')
    if ratings:
      return PublicationHouse.objects.filter(ratings=ratings)
    return PublicationHouse.objects.all()
  