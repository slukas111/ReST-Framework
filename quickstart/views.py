from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# from django.shortcuts import render
from quickstart.models import Shoe, ShoeType, ShoeColor, Manufacturer
from quickstart.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = "manufacturer"
    queryset = Manufacturer.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = "shoetype"
    queryset = ShoeType.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = "shoecolor"
    queryset = ShoeColor.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = "shoe"
    queryset = Shoe.objects.all()
