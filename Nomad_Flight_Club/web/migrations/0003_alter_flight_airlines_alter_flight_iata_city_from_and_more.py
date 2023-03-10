# Generated by Django 4.1.4 on 2022-12-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_flight_max_nights_alter_flight_min_nights_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='airlines',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='iata_city_from',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='iata_city_to',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='iata_port_from',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='iata_port_to',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='flight',
            name='iata_stopovers',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='nights',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
