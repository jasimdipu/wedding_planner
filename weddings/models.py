from django.db import models
from locations.models import Location
from partner_product_services.models import Partner, Product, Service

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200, null=True, blank=True)
    wedding_id = models.ForeignKey(
        "Wedding", null=True, blank=True, on_delete=models.SET_NULL)
    location_id = models.ForeignKey(
        Location, null=True, blank=True, on_delete=models.SET_NULL)
    start_time_planned = models.DateTimeField(null=True, blank=True)
    end_time_planned = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    budget_planned = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.event_name


class ProductIncluded(models.Model):
    # event_id = models.ForeignKey(
    #     Event, null=True, blank=True, on_delete=models.SET_NULL)
    # provides_product_id = models.ForeignKey(
    #     "ProvidesProduct", null=True, blank=True, on_delete=models.SET_NULL)
    # price = models.DecimalField(
    #     max_digits=10, decimal_places=2, null=True, blank=True)
    # current_status_id = models.ForeignKey(
    #     "Status", null=True, blank=True, on_delete=models.SET_NULL)

    # def __str__(self) -> str:
    #     return self.event_id
    pass


class ProvidesProduct(models.Model):
    # partner_id = models.ForeignKey(
    #     Partner, null=True, blank=True, on_delete=models.SET_NULL)
    # product_id = models.ForeignKey(
    #     Product, null=True, blank=True, on_delete=models.SET_NULL)
    # details = models.TextField(null=True, blank=True)

    # def __str__(self) -> str:
    #     return self.partner_id
    pass


class ProvidesService(models.Model):
    # partner_id = models.ForeignKey(
    #     Partner, null=True, blank=True, on_delete=models.SET_NULL)
    # service_id = models.ForeignKey(
    #     Service, null=True, blank=True, on_delete=models.SET_NULL)
    # details = models.TextField(null=True, blank=True)

    # def __str__(self) -> str:
    #     return self.partner_id
    pass


class ServiceIncluded(models.Model):
    # event_id = models.ForeignKey(
    #     Event, null=True, blank=True, on_delete=models.SET_NULL)
    # provides_service_id = models.ForeignKey(
    #     ProvidesService, null=True, blank=True, on_delete=models.SET_NULL)
    # price = models.DecimalField(
    #     max_digits=10, decimal_places=2, null=True, blank=True)
    # current_status_id = models.ForeignKey(
    #     "Status", null=True, blank=True, on_delete=models.SET_NULL)

    # def __str__(self) -> str:
    #     return self.event_id
    pass

class Status(models.Model):
    status_name = models.CharField(max_length=200, null=True, blank=True)
    offer = models.BooleanField(null=True, blank=True)
    offer_accepted = models.BooleanField(null=True, blank=True)
    offer_rejected = models.BooleanField(null=True, blank=True)

    def __str__(self) -> str:
        return self.status_name


class Wedding(models.Model):
    # wedding_code = models.CharField(max_length=200, null=True, blank=True)
    # start_time_planned = models.DateTimeField(null=True, blank=True)
    # end_time_planned = models.DateTimeField(null=True, blank=True)
    # start_time = models.DateTimeField(null=True, blank=True)
    # end_time = models.DateTimeField(null=True, blank=True)
    # budget_planned = models.DecimalField(
    #     max_digits=7, decimal_places=2, null=True, blank=True)

    # def __str__(self) -> str:
    #     return self.wedding_code
    pass
