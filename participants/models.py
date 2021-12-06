from django.db import models
from weddings.models import Wedding, Event
# Create your models here.


class InEvent(models.Model):
    event_id = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.SET_NULL)
    participate_id = models.ForeignKey(
        "Participate", null=True, blank=True, on_delete=models.SET_NULL)
    details = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.event_id


class Participate(models.Model):
    wedding_id = models.ForeignKey(
        Wedding, null=True, blank=True, on_delete=models.SET_NULL)
    person_id = models.ForeignKey(
        "Person", null=True, blank=True, on_delete=models.SET_NULL)


class Person(models.Model):
    person_code = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Role(models.Model):
    role_name = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self) -> str:
        return self.role_name
