# Generated by Django 4.2 on 2023-04-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory_updated_time',
            field=models.DateTimeField(default=None),
        ),
    ]