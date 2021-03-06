# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activ', '0002_auto_20160325_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Местоположение', 'verbose_name_plural': 'Местоположение'},
        ),
        migrations.AlterModelOptions(
            name='rating_a',
            options={'verbose_name': 'Доступность', 'verbose_name_plural': 'Доступность'},
        ),
        migrations.AlterModelOptions(
            name='rating_c',
            options={'verbose_name': 'Конфиденциальность', 'verbose_name_plural': 'Конфиденциальность'},
        ),
        migrations.AlterModelOptions(
            name='rating_i',
            options={'verbose_name': 'Целостность', 'verbose_name_plural': 'Целостность'},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name': 'Тип актива', 'verbose_name_plural': 'Типы активов'},
        ),
        migrations.AlterField(
            model_name='rating_a',
            name='rating',
            field=models.CharField(max_length=100, verbose_name='Оценка доступности'),
        ),
        migrations.AlterField(
            model_name='rating_c',
            name='rating',
            field=models.CharField(max_length=100, verbose_name='Оценка конфиденциальности'),
        ),
        migrations.AlterField(
            model_name='rating_i',
            name='rating',
            field=models.CharField(max_length=100, verbose_name='Оценка целостности'),
        ),
    ]
