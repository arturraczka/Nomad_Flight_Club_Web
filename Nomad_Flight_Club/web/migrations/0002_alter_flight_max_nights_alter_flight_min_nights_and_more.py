# Generated by Django 4.1.4 on 2022-12-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='max_nights',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='min_nights',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='nights',
            field=models.IntegerField(),
        ),
    ]
