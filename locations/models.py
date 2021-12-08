from django.db import models

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='cities')

    def __str__(self) -> str:
        return self.city_name


class Location(models.Model):
    location_name = models.CharField(max_length=255, blank=True, null=True)
    city_id = models.ForeignKey(
        City, null=True, blank=True, on_delete=models.SET_NULL, related_name='locations')
