# Generated by Django 4.2.1 on 2024-06-10 00:46

import dealership.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('telephone', models.CharField(max_length=10)),
                ('nit', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dealership.city')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('brand', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=11)),
                ('hp', models.FloatField()),
                ('torque', models.FloatField()),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to=dealership.models.vehicle_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleQuotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('sold', models.BooleanField(default=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership.city')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership.office')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership.vehicle')),
            ],
        ),
    ]
