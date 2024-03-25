# Generated by Django 4.2.8 on 2024-03-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualtour', '0003_tour_duration_tour_location_tour_scenes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='latitude',
            field=models.CharField(max_length=255, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='tour',
            name='longitude',
            field=models.CharField(max_length=255, null=True, verbose_name='Longitude'),
        ),
    ]
