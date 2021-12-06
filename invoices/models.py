from django.db import models
from weddings.models import Wedding, Event, Status
from partner_product_services.models import ProvidesService, ProvideProduct

# Create your models here.


class Invoice(models.Model):
    wedding_id = models.ForeignKey(
        Wedding, null=True, blank=True, on_delete=models.SET_NULL)
    time_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    invoice_amount = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    payment_date = models.TimeField(auto_now_add=True, null=True, blank=True)
    paid = models.BooleanField(null=True, blank=True)

    def __str__(self) -> str:
        return self.wedding_id


class InvoiceItem(models.Model):
    item_name = models.CharField(max_length=200, blank=True, null=True)
    item_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    invoice_id = models.ForeignKey(
        Invoice, null=True, blank=True, on_delete=models.SET_NULL)
    service_included_id = models.ForeignKey(
        "ServiceIncluded", null=True, blank=True, on_delete=models.SET_NULL)
    product_included_id = models.ForeignKey(
        "ProductIncluded", null=True, blank=True, on_delete=models.SET_NULL)


class ServiceIncluded(models.Model):
    event_id = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.SET_NULL)
    provide_services_id = models.ForeignKey(
        ProvidesService, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    current_status_id = models.ForeignKey(
        Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.event_id


class ProductIncluded(models.Model):
    event_id = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.SET_NULL)
    provides_product_id = models.ForeignKey(
        ProvideProduct, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    current_status_id = models.ForeignKey(
        Status, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.event_id
