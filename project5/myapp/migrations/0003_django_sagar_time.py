# Generated by Django 4.2.5 on 2023-10-17 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_django_sagar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='django_sagar',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]