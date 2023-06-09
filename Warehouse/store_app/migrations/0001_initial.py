# Generated by Django 4.2 on 2023-04-28 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('url', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('sku', models.CharField(max_length=10)),
                ('inventory_quantity', models.PositiveSmallIntegerField()),
                ('inventory_updated_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store', to='store_app.store')),
            ],
        ),
    ]
