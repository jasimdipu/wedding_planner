# Generated by Django 3.2.9 on 2021-12-08 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_city_country_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locations', to='locations.city'),
        ),
    ]
