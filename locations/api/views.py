from rest_framework.response import Response
from rest_framework.serializers import Serializer
from locations.models import *
from locations.api.serializer import CountrySerializers, CitySerializers, LocationSerializers
from rest_framework.generics import ListCreateAPIView


class CountryList(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CountrySerializers(queryset, many=True)
        return Response(serializer.data)


class CityList(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CitySerializers(queryset, many=True)

        return Response(serializer.data)


class LocationList(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers

    def list(self, request):
        queryset = self.get_queryset()
        serializer = LocationSerializers(queryset, many=True)
        return Response(serializer.data)
