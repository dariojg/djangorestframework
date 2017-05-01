# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='libro',
        ),
        migrations.AddField(
            model_name='libro',
            name='anio',
            field=models.IntegerField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='restapp.Autor'),
            preserve_default=False,
        ),
    ]