# Generated by Django 4.2.5 on 2023-12-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
