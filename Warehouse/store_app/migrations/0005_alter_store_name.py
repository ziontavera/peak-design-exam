# Generated by Django 4.2 on 2023-04-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_alter_product_inventory_updated_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]