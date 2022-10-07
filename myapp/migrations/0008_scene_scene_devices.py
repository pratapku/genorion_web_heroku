# Generated by Django 4.0.7 on 2022-10-07 16:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import myapp.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_firebasedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='scene',
            fields=[
                ('scene_id', models.CharField(default=myapp.utils.create_new_ref_number, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('scene_type', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='scene_devices',
            fields=[
                ('scenedevices_id', models.CharField(default=myapp.utils.create_new_ref_number, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('d_id', models.CharField(max_length=15)),
                ('scene_device_type', models.CharField(max_length=15)),
                ('status', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('time', models.DateTimeField()),
                ('scene_id', models.ForeignKey(default=1, max_length=10, on_delete=django.db.models.deletion.CASCADE, to='myapp.scene')),
            ],
        ),
    ]