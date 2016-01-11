# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 10:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutelary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('org.create', 'Can create organisations'), ('org.delete', 'Can delete organisations')),
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('parcel.list', 'Can list existing parcels'), ('parcel.view', 'Can view details of a parcel'), ('parcel.create', 'Can create parcels'), ('parcel.edit', 'Can update existing parcels'), ('parcel.delete', 'Can delete parcels')),
                'ordering': ('project', 'address'),
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('party.list', 'Can list existing parties'), ('party.view', 'Can view details of a party'), ('party.create', 'Can create parties'), ('party.edit', 'Can update existing parties'), ('party.delete', 'Can delete parties')),
                'ordering': ('project', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exampleapp.Organisation')),
            ],
            options={
                'permissions': (('project.create', 'Can create projects'), ('project.delete', 'Can delete projects')),
                'ordering': ('organisation', 'name'),
            },
        ),
        migrations.CreateModel(
            name='UserPolicyAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exampleapp.Organisation')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutelary.Policy')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exampleapp.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='party',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exampleapp.Project'),
        ),
        migrations.AddField(
            model_name='parcel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exampleapp.Project'),
        ),
    ]
