from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from quickstart.models import Shoe, ShoeType, ShoeColor, Manufacturer
from quickstart.serializers import *




class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = "manufacturer"
    queryset = Manufacturer.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = "shoetype"
    queryset = ShoeType.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = "shoecolor"
    queryset = ShoeColor.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = "shoe"
    queryset = Shoe.objects.all()
