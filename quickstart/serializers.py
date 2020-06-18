# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer 
from .models import *


# from the api documentation


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["name", "website"]


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            "style",
        ]


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            "shoe_color",
        ]


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            "size",
            "brand_name",
            "manufacturer",
            "color",
            "material",
            "shoe_type",
            "fasten_type",
        ]

