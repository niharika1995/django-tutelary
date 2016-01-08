# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('status', 'address'),
                'permissions': (('parcel.list', 'Can list existing parcels'), ('parcel.view', 'Can view details of a parcel'), ('parcel.create', 'Can create parcels'), ('parcel.edit', 'Can update existing parcels'), ('parcel.delete', 'Can delete parcels')),
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('name',),
                'permissions': (('party.list', 'Can list existing parties'), ('party.view', 'Can view details of a party'), ('party.create', 'Can create parties'), ('party.edit', 'Can update existing parties'), ('party.delete', 'Can delete parties')),
            },
        ),
    ]