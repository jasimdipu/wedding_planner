from django.urls import path
from .views import CountryList, CityList

urlpatterns = [
    path('', CountryList.as_view(), name='country-list'),
    path('city-list/', CityList.as_view(), name='city-list')
]
