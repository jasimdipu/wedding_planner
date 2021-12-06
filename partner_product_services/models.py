from django.db import models

# Create your models here.


class Partner(models.Model):
    partner_code = models.CharField(max_length=20, null=True, blank=True)
    partner_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.partner_name


class Product(models.Model):
    product_code = models.CharField(max_length=20, null=True, blank=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="static/service_image", null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.product_name


class ProvideProduct(models.Model):
    pertner_id = models.ForeignKey(
        Partner, null=True, blank=True, on_delete=models.SET_NULL)
    product_id = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)

    def __str__(self) -> str:
        return self.pertner_id


class ProvidesService(models.Model):
    pertner_id = models.ForeignKey(
        Partner, null=True, blank=True, on_delete=models.SET_NULL)
    service_id = models.ForeignKey(
        "Service", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)

    def __str__(self) -> str:
        return self.pertner_id


class Service(models.Model):
    service_code = models.CharField(max_length=20, null=True, blank=True)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="static/service_image", null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.service_name
