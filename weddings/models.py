from django.db import models

# Create your models here.


class Event(models.Model):
    pass


class ProductIncluded(models.Model):
    pass


class ProvidesProduct(models.Model):
    pass


class ProvidesService(models.Model):
    pass


class ServiceIncluded(models.Model):
    pass


class Status(models.Model):
    pass


class Wedding(models.Model):
    wedding_code = models.CharField(max_length=200, null=True, blank=True)
    start_time_planned = models.DateTimeField(null=True, blank=True)
    end_time_planned = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    budget_planned = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.wedding_code
