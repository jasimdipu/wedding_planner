from django.contrib import admin
from locations.models import *

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name']
    search_fields = ['country_name']


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'postal_code']
    search_fields = ['city_name', 'postal_code']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'city_id']
    search_fields = ['location_name']


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
