# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='asocNumber',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Association'),
        ),
    ]