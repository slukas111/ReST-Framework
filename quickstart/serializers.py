# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer 
from quickstart.models import *


# from the api documentation


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["name", "website"]


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ["style"]


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ["shoe_color"]

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    manufacturer = serializers.StringRelatedField()
    color = serializers.StringRelatedField()
    shoe_type = serializers.StringRelatedField()
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

