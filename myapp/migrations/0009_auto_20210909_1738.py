# Generated by Django 3.1.1 on 2021-09-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_threeyears'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threeyears',
            name='year1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='threeyears',
            name='year2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='threeyears',
            name='year3',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]