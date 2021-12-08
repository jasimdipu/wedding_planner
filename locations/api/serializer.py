from django.db.models import fields
from locations.models import *
from rest_framework import serializers


class CountrySerializers(serializers.ModelSerializer):
    cities = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'cities']


class CitySerializers(serializers.ModelSerializer):

    locations = serializers.StringRelatedField(many=True)

    class Meta:
        model = City
        fields = ['city_name', 'postal_code', 'locations']


class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
