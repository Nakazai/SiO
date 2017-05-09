# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-08 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=254)),
                ('sentTime', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.CharField(max_length=254)),
                ('message', models.TextField()),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Association')),
            ],
            options={
                'db_table': 'Email',
            },
        ),
    ]
