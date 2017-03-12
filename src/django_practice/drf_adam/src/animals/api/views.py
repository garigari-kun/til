from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from animals.models import Kitten, Puppy
from .serializers import KittenSerializer, PuppySerializer


class KittenViewSet(ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer


class PuppyListCreateView(generics.ListCreateAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer


class PuppyDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
