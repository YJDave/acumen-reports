# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-04 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrations.ProfileAuth'),
        ),
        migrations.DeleteModel(
            name='ProfileAuth',
        ),
    ]