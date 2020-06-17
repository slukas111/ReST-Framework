from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


# from the api documentation


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["name", "website"]


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            "style",
        ]


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            "shoe_color",
        ]


class ShoeSerializer(ModelSerializer):
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

