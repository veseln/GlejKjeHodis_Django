# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-11 16:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppBackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField()),
                ('city', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='path',
            name='locations',
            field=models.ManyToManyField(related_name='locations', to='AppBackend.Location'),
        ),
        migrations.AddField(
            model_name='path',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paths', to=settings.AUTH_USER_MODEL),
        ),
    ]
