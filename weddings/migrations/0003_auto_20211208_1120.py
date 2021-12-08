# Generated by Django 3.2.9 on 2021-12-08 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('weddings', '0002_event_productincluded_providesproduct_providesservice_serviceincluded_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wedding',
            name='budget_planned',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='end_time_planned',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='start_time_planned',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='wedding_code',
        ),
        migrations.AddField(
            model_name='event',
            name='budget_planned',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time_planned',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.location'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time_planned',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='wedding_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weddings.wedding'),
        ),
        migrations.AddField(
            model_name='status',
            name='offer',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='offer_accepted',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='offer_rejected',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='status_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
