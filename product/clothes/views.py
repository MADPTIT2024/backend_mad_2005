from rest_framework import generics
from .models import Styles, Producer, Cloth
from .serializers import StylesSerializer, ClothSerializer, ProducerSerializer


class StylesListCreate(generics.ListCreateAPIView):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer


class StylesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Styles.objects.all()
    serializer_class = StylesSerializer


class ProducerListCreate(generics.ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProducerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ClothListCreate(generics.ListCreateAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer


class ClothRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
